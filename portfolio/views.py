from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.http import Http404, HttpResponse, JsonResponse
from .content import CONTENT, DEFAULT_LANG
from .forms import ContactForm
from .models import Post, Project, SiteSettings  # SiteSettings به اینجا منتقل شد


def _lang(lang):
    if lang not in CONTENT:
        raise Http404
    return lang


def _ctx(request, lang, url_name, **kw):
    request.session["lang"] = lang
    
    settings_obj = SiteSettings.objects.first() or SiteSettings()
    
    # themes list
    themes = [
        {
            "key": t["key"],
            "label": t["label_fa"] if lang == "fa" else t["label_en"],
            "color": t["color"],
        }
        for t in THEMES
    ]
    
    return {
        "c": CONTENT[lang],
        "lang": lang,
        "dir": "rtl" if lang == "fa" else "ltr",
        "site_settings": settings_obj,
        "themes": themes,
        "url_en": reverse(url_name, kwargs={**kw.get("kwargs", {}), "lang": "en"}),
        "url_fa": reverse(url_name, kwargs={**kw.get("kwargs", {}), "lang": "fa"}),
        **{k: v for k, v in kw.items() if k != "kwargs"},
    }

def _project_card(p, lang, i=0):
    main_image = p.image.url if p.image else None
    
    # گرفتن لیست همه عکس‌های گالری
    gallery_images = []
    for img in p.images.all():
        gallery_images.append({
            "url": img.image.url,
            "alt": img.alt_text_fa if lang == "fa" else img.alt_text_en
        })
    
    # اگر عکس کاور خالی بود، اولین عکس گالری را کاور کن
    if not main_image and gallery_images:
        main_image = gallery_images[0]["url"]

    return {
        "title": p.tr("title", lang),
        "kind": p.tr("kind", lang),
        "desc": p.tr("desc", lang),
        "did": p.tr("did", lang),
        "tags": p.tag_list(lang),
        "url": reverse("portfolio:project", args=[lang, p.slug]),
        "link": p.link,
        "image": main_image,
        "gallery": gallery_images,
        "shade": i % 3 + 1,
    }


def _post_card(p, lang):
    return {
        "title": p.tr("title", lang),
        "excerpt": p.tr("excerpt", lang),
        "image": p.image.url if p.image else "",
        "date": p.created_at,
        "url": reverse("portfolio:post", args=[lang, p.slug]),
    }


def root_redirect(request):
    lang = request.session.get("lang", DEFAULT_LANG)
    return redirect("portfolio:home", lang=lang if lang in CONTENT else DEFAULT_LANG)


from .models import Experience, Post, Project, SiteSettings

def _experience_card(e, lang):
    return {
        "role": e.tr("role", lang),
        "company": e.tr("company", lang),
        "location": e.tr("location", lang),
        "period": e.tr("period", lang),
        "bullets": e.bullets(lang),
        "tags": e.tag_list(lang),
        "link": e.link,
    }

def home(request, lang):
    lang = _lang(lang)
    projects = [_project_card(p, lang, i) for i, p in enumerate(Project.objects.filter(published=True))]
    experiences = [_experience_card(e, lang) for e in Experience.objects.filter(published=True)]
    pdf_mode = request.GET.get("pdf") == "1"
    posts = [] if pdf_mode else [_post_card(p, lang) for p in Post.objects.filter(published=True)[:3]]
    return render(request, "portfolio/index.html",
                  _ctx(request, lang, "portfolio:home", projects=projects, posts=posts,
                       experiences=experiences, pdf_mode=pdf_mode))

def project_detail(request, lang, slug):
    lang = _lang(lang)
    p = get_object_or_404(Project, slug=slug, published=True)
    others = [_project_card(o, lang, i) for i, o in
              enumerate(Project.objects.filter(published=True).exclude(pk=p.pk)[:2])]
    
    gallery_images = [
        {
            "url": img.image.url,
            "alt": img.alt_text_fa if lang == "fa" else img.alt_text_en
        }
        for img in p.images.all()
    ]

    ctx = _ctx(request, lang, "portfolio:project", kwargs={"slug": slug},
               p={
                   **_project_card(p, lang), 
                   "body": p.tr("body", lang) or p.tr("desc", lang),
                   "gallery": gallery_images
               },
               others=others)
    return render(request, "portfolio/project_detail.html", ctx)


def blog_list(request, lang):
    lang = _lang(lang)
    posts = [_post_card(p, lang) for p in Post.objects.filter(published=True)]
    return render(request, "portfolio/blog_list.html",
                  _ctx(request, lang, "portfolio:blog", posts=posts))


def blog_detail(request, lang, slug):
    lang = _lang(lang)
    p = get_object_or_404(Post, slug=slug, published=True)
    ctx = _ctx(request, lang, "portfolio:post", kwargs={"slug": slug},
               post={**_post_card(p, lang), "body": p.tr("body", lang)})
    return render(request, "portfolio/blog_detail.html", ctx)


@require_POST
def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({"ok": True})
    return JsonResponse({"ok": False, "errors": form.errors}, status=400)


def projects_list(request, lang):
    lang = _lang(lang)
    all_projects = Project.objects.filter(published=True)
    projects = [_project_card(p, lang, i) for i, p in enumerate(all_projects)]
    return render(request, "portfolio/projects_list.html", 
                  _ctx(request, lang, "portfolio:projects_list", projects=projects))




from .content import CONTENT, DEFAULT_LANG, THEMES

def set_theme(request, theme_key):
    """ذخیره تم در سشن و برگشت به همان صفحه."""
    from .content import THEMES as T
    valid = {t["key"] for t in T}
    if theme_key in valid:
        request.session["theme"] = theme_key
    # back to referring page or home
    next_url = request.META.get("HTTP_REFERER") or reverse(
        "portfolio:home", kwargs={"lang": request.session.get("lang", DEFAULT_LANG)}
    )
    return redirect(next_url)




def export_pdf(request, lang):
    lang = _lang(lang)
    url = request.build_absolute_uri(reverse("portfolio:home", kwargs={"lang": lang})) + "?pdf=1"
    try:
        from .pdf import render_pdf
        data = render_pdf(url, cookies=request.COOKIES)
    except RuntimeError as e:      # مرورگر پیدا نشد
        return HttpResponse(str(e), status=500, content_type="text/plain; charset=utf-8")
    except ImportError:
        
        return HttpResponse("pip install playwright\nplaywright install chromium",
                            status=500, content_type="text/plain; charset=utf-8")
    resp = HttpResponse(data, content_type="application/pdf")
    resp["Content-Disposition"] = f'attachment; filename="portfolio-{lang}.pdf"'
    return resp