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






# ⬇️ این کلاس را به انتهای فایل اضافه کنید ⬇️
class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, 
        related_name="images", 
        on_delete=models.CASCADE, 
        verbose_name="پروژه"
    )
    image = models.ImageField("تصویر", upload_to="projects/gallery/")
    alt_text_fa = models.CharField("متن جایگزین (فارسی)", max_length=200, blank=True)
    alt_text_en = models.CharField("متن جایگزین (انگلیسی)", max_length=200, blank=True)
    order = models.PositiveIntegerField("ترتیب", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "تصویر پروژه"
        verbose_name_plural = "تصاویر پروژه"

    def __str__(self):
        return f"تصویر برای {self.project.title_en} ({self.id})"




class SiteSettings(models.Model):
    phone = models.CharField("شماره تماس", max_length=40, blank=True)
    email = models.EmailField("ایمیل", blank=True)
    linkedin = models.URLField("لینک لینکدین", blank=True)
    instagram = models.URLField("لینک اینستاگرام", blank=True)
    github = models.URLField("لینک گیت‌هاب", blank=True)
    telegram = models.URLField("لینک تلگرام", blank=True)

    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "تنظیمات سایت"

    def __str__(self):
        return "تنظیمات کلی سایت"




class Experience(Bilingual):
    order = models.PositiveIntegerField("ترتیب", default=0, help_text="عدد کمتر = بالاتر (جدیدترین سابقه را 0 بگذارید)")
    published = models.BooleanField("منتشر شده", default=True)
    link = models.URLField("وب‌سایت شرکت", blank=True)

    company_en = models.CharField("Company (EN)", max_length=160)
    company_fa = models.CharField("نام شرکت (فارسی)", max_length=160, blank=True)
    role_en = models.CharField("Role (EN)", max_length=160)
    role_fa = models.CharField("عنوان شغلی (فارسی)", max_length=160, blank=True)
    location_en = models.CharField("Location (EN)", max_length=120, blank=True)
    location_fa = models.CharField("محل (فارسی)", max_length=120, blank=True)
    period_en = models.CharField("Period (EN)", max_length=80, help_text="مثلاً: 2022 — Present")
    period_fa = models.CharField("بازه‌ی زمانی (فارسی)", max_length=80, blank=True, help_text="مثلاً: ۱۴۰۱ — اکنون")
    desc_en = models.TextField("Responsibilities (EN)", blank=True, help_text="هر خط یک مورد (بولت) می‌شود")
    desc_fa = models.TextField("شرح وظایف و دستاوردها (فارسی)", blank=True, help_text="هر خط یک مورد (بولت) می‌شود")
    tags_en = models.CharField("Tech (EN)", max_length=200, blank=True, help_text="با ویرگول جدا کنید")
    tags_fa = models.CharField("فناوری‌ها (فارسی)", max_length=200, blank=True, help_text="با ویرگول جدا کنید")

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "سابقه کاری"
        verbose_name_plural = "سوابق کاری"

    def __str__(self):
        return f"{self.role_en} @ {self.company_en}"

    def bullets(self, lang):
        lines = self.tr("desc", lang).splitlines()
        return [l.strip().lstrip("-•*– ").strip() for l in lines if l.strip()]

    def tag_list(self, lang):
        raw = self.tr("tags", lang).replace("،", ",")
        return [t.strip() for t in raw.split(",") if t.strip()]




class Certificate(Bilingual):
    order = models.PositiveIntegerField("ترتیب", default=0, help_text="عدد کمتر = بالاتر")
    published = models.BooleanField("منتشر شده", default=True)
    image = models.ImageField("تصویر گواهینامه", upload_to="certificates/", blank=True)
    link = models.URLField("لینک اعتبارسنجی", blank=True, help_text="مثلاً لینک Credly یا سایت صادرکننده")

    title_en = models.CharField("Title (EN)", max_length=200)
    title_fa = models.CharField("عنوان (فارسی)", max_length=200, blank=True)
    issuer_en = models.CharField("Issuer (EN)", max_length=160, help_text="مثلاً: Microsoft / Coursera")
    issuer_fa = models.CharField("صادرکننده (فارسی)", max_length=160, blank=True)
    date_en = models.CharField("Date (EN)", max_length=40, help_text="مثلاً: 2024")
    date_fa = models.CharField("تاریخ (فارسی)", max_length=40, blank=True, help_text="مثلاً: ۱۴۰۳")
    desc_en = models.TextField("Description (EN)", blank=True)
    desc_fa = models.TextField("توضیح (فارسی)", blank=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "گواهینامه / افتخار"
        verbose_name_plural = "گواهینامه‌ها و افتخارات"

    def __str__(self):
        return self.title_en