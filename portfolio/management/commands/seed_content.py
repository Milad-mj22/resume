from django.core.management.base import BaseCommand
from portfolio.models import SiteSettings
from portfolio.content import CONTENT

class Command(BaseCommand):
    help = "Seed SiteSettings from content.py CONTENT"

    def handle(self, *args, **kwargs):
        s = SiteSettings.load()
        en = CONTENT["en"]
        fa = CONTENT["fa"]

        def set_bi(field, en_val, fa_val):
            setattr(s, f"{field}_en", en_val)
            setattr(s, f"{field}_fa", fa_val)

        # هویتی
        set_bi("name", en["name"], fa["name"])
        set_bi("brand", en["brand"], fa["brand"])
        set_bi("page_title", en["title"], fa["title"])
        set_bi("lang_label", en["lang_label"], fa["lang_label"])
        set_bi("flag", en["flag"], fa["flag"])
        set_bi("cta", en["cta"], fa["cta"])
        set_bi("footer", en["footer"], fa["footer"])

        # Hero
        for k in ["eyebrow", "hey", "line1", "line2", "text", "link"]:
            set_bi(f"hero_{k}", en["hero"][k], fa["hero"][k])

        # About
        for k in ["eyebrow", "title_a", "title_b", "lead", "text", "cta"]:
            set_bi(f"about_{k}", en["about"][k], fa["about"][k])

        # Work
        for k in ["eyebrow", "title", "label"]:
            set_bi(f"work_{k}", en["work"][k], fa["work"][k])

        # Reviews
        set_bi("reviews_eyebrow", en["reviews"]["eyebrow"], fa["reviews"]["eyebrow"])
        set_bi("reviews_title", en["reviews"]["title"], fa["reviews"]["title"])

        # Contact
        for k in ["eyebrow", "title", "text", "name", "phone", "email",
                  "project", "message", "submit", "sending", "success", "error"]:
            set_bi(f"contact_{k}", en["contact"][k], fa["contact"][k])

        # Skills title
        set_bi("skills_title", en["skills_title"], fa["skills_title"])

        # Experience / Certificates headers
        set_bi("exp_eyebrow", en["experience"]["eyebrow"], fa["experience"]["eyebrow"])
        set_bi("exp_title", en["experience"]["title"], fa["experience"]["title"])
        set_bi("cert_eyebrow", en["certificates"]["eyebrow"], fa["certificates"]["eyebrow"])
        set_bi("cert_title", en["certificates"]["title"], fa["certificates"]["title"])

        # UI
        for k in ["blog", "blog_eyebrow", "blog_title", "blog_text", "blog_empty",
                  "read_more", "back_blog", "back_work", "visit", "overview",
                  "more_work", "latest", "all_posts", "all_projects", "pdf"]:
            set_bi(f"ui_{k}", en["ui"][k], fa["ui"][k])

        # JSON lists
        s.nav_items = [{"id": i, "en": e, "fa": f} for (i, e), (_, f) in zip(en["nav"], fa["nav"])]
        s.stats = [
            {"en": e[0], "fa": f[0], "label_en": e[1], "label_fa": f[1]}
            for e, f in zip(en["stats"], fa["stats"])
        ]
        s.skills = [
            {"en": e[0], "fa": f[0], "level": e[1]}
            for e, f in zip(en["skills"], fa["skills"])
        ]
        s.reviews = [
            {
                "text_en": e["text"], "text_fa": f["text"],
                "name_en": e["name"], "name_fa": f["name"],
                "role_en": e["role"], "role_fa": f["role"],
            }
            for e, f in zip(en["reviews"]["items"], fa["reviews"]["items"])
        ]
        s.project_options = fa["contact"]["project_options"]  # یا ساختار dict

        s.save()
        self.stdout.write(self.style.SUCCESS("✅ SiteSettings seeded successfully."))