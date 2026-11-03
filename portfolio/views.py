from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from .content import CONTENT, DEFAULT_LANG
from .forms import ContactForm
from .models import Post, Project


def _lang(lang):
    if lang not in CONTENT:
        raise Http404
    return lang


def _ctx(request, lang, url_name, **kw):
    """کانتکست مشترک؛ url_en / url_fa برای دکمه تغییر زبان در همان صفحه."""
    request.session["lang"] = lang
    return {
        "c": CONTENT[lang],
        "lang": lang,
        "dir": "rtl" if lang == "fa" else "ltr",
        "url_en": reverse(url_name, kwargs={**kw.get("kwargs", {}), "lang": "en"}),
        "url_fa": reverse(url_name, kwargs={**kw.get("kwargs", {}), "lang": "fa"}),
        **{k: v for k, v in kw.items() if k != "kwargs"},
    }


def _project_card(p, lang, i=0):
    return {
        "title": p.tr("title", lang),
        "kind": p.tr("kind", lang),
        "desc": p.tr("desc", lang),
        "did": p.tr("did", lang),
        "tags": p.tag_list(lang),
        "image": p.image.url if p.image else "",
        "url": reverse("portfolio:project", args=[lang, p.slug]),
        "link": p.link,
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


def home(request, lang):
    lang = _lang(lang)
    projects = [_project_card(p, lang, i) for i, p in enumerate(Project.objects.filter(published=True))]
    posts = [_post_card(p, lang) for p in Post.objects.filter(published=True)[:3]]
    return render(request, "portfolio/index.html",
                  _ctx(request, lang, "portfolio:home", projects=projects, posts=posts))


def project_detail(request, lang, slug):
    lang = _lang(lang)
    p = get_object_or_404(Project, slug=slug, published=True)
    others = [_project_card(o, lang, i) for i, o in
              enumerate(Project.objects.filter(published=True).exclude(pk=p.pk)[:2])]
    ctx = _ctx(request, lang, "portfolio:project", kwargs={"slug": slug},
               p={**_project_card(p, lang), "body": p.tr("body", lang) or p.tr("desc", lang)},
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
