from django.db import models


class Bilingual(models.Model):
    """کمک‌کننده برای فیلدهای دوزبانه: tr("title", "fa")"""

    class Meta:
        abstract = True

    def tr(self, name, lang):
        other = "en" if lang == "fa" else "fa"
        return getattr(self, f"{name}_{lang}") or getattr(self, f"{name}_{other}")


class ContactMessage(models.Model):
    name = models.CharField("نام", max_length=120)
    phone = models.CharField("شماره تماس", max_length=40, blank=True)
    email = models.EmailField("ایمیل")
    project_type = models.CharField("نوع پروژه", max_length=120, blank=True)
    message = models.TextField("پیام")
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField("خوانده شده", default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "پیام تماس"
        verbose_name_plural = "پیام‌های تماس"

    def __str__(self):
        return f"{self.name} — {self.email}"


class Project(Bilingual):
    slug = models.SlugField("اسلاگ (آدرس)", unique=True)
    order = models.PositiveIntegerField("ترتیب", default=0)
    published = models.BooleanField("منتشر شده", default=True)
    image = models.ImageField("تصویر شاخص", upload_to="projects/", blank=True)
    link = models.URLField("لینک پروژه", blank=True)

    title_en = models.CharField("Title (EN)", max_length=120)
    title_fa = models.CharField("عنوان (فارسی)", max_length=120, blank=True)
    kind_en = models.CharField("Type (EN)", max_length=160, blank=True)
    kind_fa = models.CharField("نوع (فارسی)", max_length=160, blank=True)
    desc_en = models.TextField("Short description (EN)")
    desc_fa = models.TextField("توضیح کوتاه (فارسی)", blank=True)
    did_en = models.TextField("What I did (EN)", blank=True)
    did_fa = models.TextField("کار من (فارسی)", blank=True)
    body_en = models.TextField("Case study (EN)", blank=True, help_text="هر پاراگراف را با یک خط خالی جدا کنید")
    body_fa = models.TextField("شرح کامل (فارسی)", blank=True, help_text="هر پاراگراف را با یک خط خالی جدا کنید")
    tags_en = models.CharField("Tags (EN)", max_length=200, blank=True, help_text="با ویرگول جدا کنید")
    tags_fa = models.CharField("تگ‌ها (فارسی)", max_length=200, blank=True, help_text="با ویرگول فارسی یا انگلیسی جدا کنید")

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه‌ها"

    def __str__(self):
        return self.title_en

    def tag_list(self, lang):
        raw = self.tr("tags", lang).replace("،", ",")
        return [t.strip() for t in raw.split(",") if t.strip()]


class Post(Bilingual):
    slug = models.SlugField("اسلاگ (آدرس)", unique=True)
    published = models.BooleanField("منتشر شده", default=True)
    image = models.ImageField("تصویر شاخص", upload_to="posts/", blank=True)
    created_at = models.DateTimeField("تاریخ انتشار", auto_now_add=True)

    title_en = models.CharField("Title (EN)", max_length=160)
    title_fa = models.CharField("عنوان (فارسی)", max_length=160, blank=True)
    excerpt_en = models.TextField("Excerpt (EN)", blank=True)
    excerpt_fa = models.TextField("خلاصه (فارسی)", blank=True)
    body_en = models.TextField("Body (EN)", help_text="هر پاراگراف را با یک خط خالی جدا کنید")
    body_fa = models.TextField("متن (فارسی)", blank=True, help_text="هر پاراگراف را با یک خط خالی جدا کنید")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله‌های وبلاگ"

    def __str__(self):
        return self.title_en
