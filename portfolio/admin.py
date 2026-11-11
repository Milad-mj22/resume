from django.contrib import admin
from .models import ContactMessage, Post, Project, SiteSettings

from django.contrib import admin
from .models import Project, ProjectImage

# ⬇️ این کلاس را اضافه کنید ⬇️
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # تعداد فیلدهای خالی که برای آپلود عکس جدید نشان داده می‌شود


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "project_type", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    list_editable = ("is_read",)
    search_fields = ("name", "email", "message")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title_en", "title_fa", "order", "published")
    inlines = [ProjectImageInline]
    list_editable = ("order", "published")
    prepopulated_fields = {"slug": ("title_en",)}
    fieldsets = (
        (None, {"fields": ("slug", "order", "published", "image", "link")}),
        ("English", {"fields": ("title_en", "kind_en", "desc_en", "did_en", "body_en", "tags_en")}),
        ("فارسی", {"fields": ("title_fa", "kind_fa", "desc_fa", "did_fa", "body_fa", "tags_fa")}),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title_en", "title_fa", "created_at", "published")
    list_editable = ("published",)
    prepopulated_fields = {"slug": ("title_en",)}
    fieldsets = (
        (None, {"fields": ("slug", "published", "image")}),
        ("English", {"fields": ("title_en", "excerpt_en", "body_en")}),
        ("فارسی", {"fields": ("title_fa", "excerpt_fa", "body_fa")}),
    )





from django.contrib import admin
from django.utils.html import format_html
from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False  # نگذاریم حذف شود

    fieldsets = (
        ("🌐 هویتی و برند", {
            "fields": (
                "name_en", "name_fa", "brand_en", "brand_fa",
                "page_title_en", "page_title_fa",
                "lang_label_en", "lang_label_fa",
                "flag_en", "flag_fa",
                "cta_en", "cta_fa",
                "footer_en", "footer_fa",
            )
        }),
        ("🏠 Hero", {
            "fields": (
                "hero_eyebrow_en", "hero_eyebrow_fa",
                "hero_hey_en", "hero_hey_fa",
                "hero_line1_en", "hero_line1_fa",
                "hero_line2_en", "hero_line2_fa",
                "hero_text_en", "hero_text_fa",
                "hero_link_en", "hero_link_fa",
            )
        }),
        ("📖 About", {
            "fields": (
                "about_eyebrow_en", "about_eyebrow_fa",
                "about_title_a_en", "about_title_a_fa",
                "about_title_b_en", "about_title_b_fa",
                "about_lead_en", "about_lead_fa",
                "about_text_en", "about_text_fa",
                "about_cta_en", "about_cta_fa",
            )
        }),
        ("📊 عناوین بخش‌ها", {
            "fields": (
                "skills_title_en", "skills_title_fa",
                "work_eyebrow_en", "work_eyebrow_fa",
                "work_title_en", "work_title_fa",
                "work_label_en", "work_label_fa",
                "reviews_eyebrow_en", "reviews_eyebrow_fa",
                "reviews_title_en", "reviews_title_fa",
                "exp_eyebrow_en", "exp_eyebrow_fa",
                "exp_title_en", "exp_title_fa",
                "cert_eyebrow_en", "cert_eyebrow_fa",
                "cert_title_en", "cert_title_fa",
            )
        }),
        ("✉️ Contact", {
            "fields": (
                "contact_eyebrow_en", "contact_eyebrow_fa",
                "contact_title_en", "contact_title_fa",
                "contact_text_en", "contact_text_fa",
                "contact_name_en", "contact_name_fa",
                "contact_phone_en", "contact_phone_fa",
                "contact_email_en", "contact_email_fa",
                "contact_project_en", "contact_project_fa",
                "contact_message_en", "contact_message_fa",
                "contact_submit_en", "contact_submit_fa",
                "contact_sending_en", "contact_sending_fa",
                "contact_success_en", "contact_success_fa",
                "contact_error_en", "contact_error_fa",
            )
        }),
        ("🏷️ UI Labels", {
            "fields": (
                "ui_blog_en", "ui_blog_fa",
                "ui_blog_eyebrow_en", "ui_blog_eyebrow_fa",
                "ui_blog_title_en", "ui_blog_title_fa",
                "ui_blog_text_en", "ui_blog_text_fa",
                "ui_blog_empty_en", "ui_blog_empty_fa",
                "ui_read_more_en", "ui_read_more_fa",
                "ui_back_blog_en", "ui_back_blog_fa",
                "ui_back_work_en", "ui_back_work_fa",
                "ui_visit_en", "ui_visit_fa",
                "ui_overview_en", "ui_overview_fa",
                "ui_more_work_en", "ui_more_work_fa",
                "ui_latest_en", "ui_latest_fa",
                "ui_all_posts_en", "ui_all_posts_fa",
                "ui_all_projects_en", "ui_all_projects_fa",
                "ui_pdf_en", "ui_pdf_fa",
            )
        }),
        ("📋 لیست‌ها (JSON)", {
            "fields": ("nav_items", "stats", "skills", "reviews", "project_options"),
            "description": "این فیلدها را به صورت JSON ویرایش کنید. ساختار در help_text هر فیلد آمده است."
        }),
        ("🔗 شبکه‌های اجتماعی", {
            "fields": ("phone", "email", "linkedin", "instagram", "github", "telegram")
        }),
    )

from .models import ContactMessage, Experience, Post, Project, SiteSettings   # Experience اضافه شد

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role_en", "company_en", "period_en", "order", "published")
    list_editable = ("order", "published")
    fieldsets = (
        (None, {"fields": ("order", "published", "link")}),
        ("English", {"fields": ("role_en", "company_en", "location_en", "period_en", "desc_en", "tags_en")}),
        ("فارسی", {"fields": ("role_fa", "company_fa", "location_fa", "period_fa", "desc_fa", "tags_fa")}),
    )



from .models import Certificate

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("title_en", "issuer_en", "date_en", "order", "published")
    list_editable = ("order", "published")
    fieldsets = (
        (None, {"fields": ("order", "published", "image", "link")}),
        ("English", {"fields": ("title_en", "issuer_en", "date_en", "desc_en")}),
        ("فارسی", {"fields": ("title_fa", "issuer_fa", "date_fa", "desc_fa")}),
    )