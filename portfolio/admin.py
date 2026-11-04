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





@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # جلوگیری از ساخت بیش از یک رکورد تنظیمات
        return not SiteSettings.objects.exists()



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