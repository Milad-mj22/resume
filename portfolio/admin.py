from django.contrib import admin
from .models import ContactMessage, Post, Project

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



