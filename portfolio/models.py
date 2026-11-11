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




from django.db import models

# --- بقیه مدل‌ها بدون تغییر ---

class SiteSettings(Bilingual):
    """
    Singleton — تنها یک رکورد. همه فیلدهای هویتی و متنی اینجا هستند.
    هر فیلد دوزبانه: _en و _fa
    """

    # ==== برند و هویتی ====
    name_en = models.CharField("Name (EN)", max_length=120, blank=True)
    name_fa = models.CharField("نام (فارسی)", max_length=120, blank=True)
    brand_en = models.CharField("Brand (EN)", max_length=120, blank=True)
    brand_fa = models.CharField("برند (فارسی)", max_length=120, blank=True)
    page_title_en = models.CharField("Page title (EN)", max_length=200, blank=True)
    page_title_fa = models.CharField("عنوان صفحه (فارسی)", max_length=200, blank=True)
    lang_label_en = models.CharField("Language label (EN)", max_length=60, blank=True, default="English")
    lang_label_fa = models.CharField("برچسب زبان (فارسی)", max_length=60, blank=True, default="فارسی")
    flag_en = models.CharField("Flag (EN)", max_length=16, blank=True, default="🇺🇸")
    flag_fa = models.CharField("پرچم (فارسی)", max_length=16, blank=True, default="🇮🇷")
    cta_en = models.CharField("CTA (EN)", max_length=80, blank=True)
    cta_fa = models.CharField("دعوت به اقدام (فارسی)", max_length=80, blank=True)
    footer_en = models.CharField("Footer (EN)", max_length=200, blank=True)
    footer_fa = models.CharField("فوتر (فارسی)", max_length=200, blank=True)

    # ==== Hero ====
    hero_eyebrow_en = models.CharField(max_length=120, blank=True)
    hero_eyebrow_fa = models.CharField(max_length=120, blank=True)
    hero_hey_en = models.CharField(max_length=120, blank=True)
    hero_hey_fa = models.CharField(max_length=120, blank=True)
    hero_line1_en = models.CharField(max_length=200, blank=True)
    hero_line1_fa = models.CharField(max_length=200, blank=True)
    hero_line2_en = models.CharField(max_length=200, blank=True)
    hero_line2_fa = models.CharField(max_length=200, blank=True)
    hero_text_en = models.TextField(blank=True)
    hero_text_fa = models.TextField(blank=True)
    hero_link_en = models.CharField(max_length=120, blank=True)
    hero_link_fa = models.CharField(max_length=120, blank=True)

    # ==== About ====
    about_eyebrow_en = models.CharField(max_length=120, blank=True)
    about_eyebrow_fa = models.CharField(max_length=120, blank=True)
    about_title_a_en = models.CharField(max_length=200, blank=True)
    about_title_a_fa = models.CharField(max_length=200, blank=True)
    about_title_b_en = models.CharField(max_length=200, blank=True)
    about_title_b_fa = models.CharField(max_length=200, blank=True)
    about_lead_en = models.TextField(blank=True)
    about_lead_fa = models.TextField(blank=True)
    about_text_en = models.TextField(blank=True)
    about_text_fa = models.TextField(blank=True)
    about_cta_en = models.CharField(max_length=80, blank=True)
    about_cta_fa = models.CharField(max_length=80, blank=True)

    # ==== عناوین بخش‌ها ====
    skills_title_en = models.CharField(max_length=160, blank=True)
    skills_title_fa = models.CharField(max_length=160, blank=True)
    work_eyebrow_en = models.CharField(max_length=120, blank=True)
    work_eyebrow_fa = models.CharField(max_length=120, blank=True)
    work_title_en = models.CharField(max_length=200, blank=True)
    work_title_fa = models.CharField(max_length=200, blank=True)
    work_label_en = models.CharField(max_length=80, blank=True)
    work_label_fa = models.CharField(max_length=80, blank=True)

    # ==== Reviews ====
    reviews_eyebrow_en = models.CharField(max_length=120, blank=True)
    reviews_eyebrow_fa = models.CharField(max_length=120, blank=True)
    reviews_title_en = models.CharField(max_length=200, blank=True)
    reviews_title_fa = models.CharField(max_length=200, blank=True)

    # ==== Contact ====
    contact_eyebrow_en = models.CharField(max_length=200, blank=True)
    contact_eyebrow_fa = models.CharField(max_length=200, blank=True)
    contact_title_en = models.CharField(max_length=160, blank=True)
    contact_title_fa = models.CharField(max_length=160, blank=True)
    contact_text_en = models.TextField(blank=True)
    contact_text_fa = models.TextField(blank=True)
    contact_name_en = models.CharField(max_length=80, blank=True)
    contact_name_fa = models.CharField(max_length=80, blank=True)
    contact_phone_en = models.CharField(max_length=80, blank=True)
    contact_phone_fa = models.CharField(max_length=80, blank=True)
    contact_email_en = models.CharField(max_length=80, blank=True)
    contact_email_fa = models.CharField(max_length=80, blank=True)
    contact_project_en = models.CharField(max_length=120, blank=True)
    contact_project_fa = models.CharField(max_length=120, blank=True)
    contact_message_en = models.CharField(max_length=80, blank=True)
    contact_message_fa = models.CharField(max_length=80, blank=True)
    contact_submit_en = models.CharField(max_length=80, blank=True)
    contact_submit_fa = models.CharField(max_length=80, blank=True)
    contact_sending_en = models.CharField(max_length=80, blank=True)
    contact_sending_fa = models.CharField(max_length=80, blank=True)
    contact_success_en = models.CharField(max_length=200, blank=True)
    contact_success_fa = models.CharField(max_length=200, blank=True)
    contact_error_en = models.CharField(max_length=200, blank=True)
    contact_error_fa = models.CharField(max_length=200, blank=True)

    # ==== UI labels ====
    ui_blog_en = models.CharField(max_length=80, blank=True)
    ui_blog_fa = models.CharField(max_length=80, blank=True)
    ui_blog_eyebrow_en = models.CharField(max_length=80, blank=True)
    ui_blog_eyebrow_fa = models.CharField(max_length=80, blank=True)
    ui_blog_title_en = models.CharField(max_length=200, blank=True)
    ui_blog_title_fa = models.CharField(max_length=200, blank=True)
    ui_blog_text_en = models.TextField(blank=True)
    ui_blog_text_fa = models.TextField(blank=True)
    ui_blog_empty_en = models.CharField(max_length=200, blank=True)
    ui_blog_empty_fa = models.CharField(max_length=200, blank=True)
    ui_read_more_en = models.CharField(max_length=80, blank=True)
    ui_read_more_fa = models.CharField(max_length=80, blank=True)
    ui_back_blog_en = models.CharField(max_length=80, blank=True)
    ui_back_blog_fa = models.CharField(max_length=80, blank=True)
    ui_back_work_en = models.CharField(max_length=80, blank=True)
    ui_back_work_fa = models.CharField(max_length=80, blank=True)
    ui_visit_en = models.CharField(max_length=80, blank=True)
    ui_visit_fa = models.CharField(max_length=80, blank=True)
    ui_overview_en = models.CharField(max_length=80, blank=True)
    ui_overview_fa = models.CharField(max_length=80, blank=True)
    ui_more_work_en = models.CharField(max_length=80, blank=True)
    ui_more_work_fa = models.CharField(max_length=80, blank=True)
    ui_latest_en = models.CharField(max_length=80, blank=True)
    ui_latest_fa = models.CharField(max_length=80, blank=True)
    ui_all_posts_en = models.CharField(max_length=80, blank=True)
    ui_all_posts_fa = models.CharField(max_length=80, blank=True)
    ui_all_projects_en = models.CharField(max_length=80, blank=True)
    ui_all_projects_fa = models.CharField(max_length=80, blank=True)
    ui_pdf_en = models.CharField(max_length=40, blank=True)
    ui_pdf_fa = models.CharField(max_length=40, blank=True)

    # ==== Experience / Certificates عناوین بخش ====
    exp_eyebrow_en = models.CharField(max_length=80, blank=True)
    exp_eyebrow_fa = models.CharField(max_length=80, blank=True)
    exp_title_en = models.CharField(max_length=160, blank=True)
    exp_title_fa = models.CharField(max_length=160, blank=True)
    cert_eyebrow_en = models.CharField(max_length=80, blank=True)
    cert_eyebrow_fa = models.CharField(max_length=80, blank=True)
    cert_title_en = models.CharField(max_length=160, blank=True)
    cert_title_fa = models.CharField(max_length=160, blank=True)

    # ==== لیست‌ها با JsonField ====
    # ساختار: [{"en": "...", "fa": "...", ...}, ...]
    nav_items = models.JSONField(
        "منوی ناوبری", default=list, blank=True,
        help_text='[{"id":"about","en":"About","fa":"درباره"}, ...]'
    )
    stats = models.JSONField(
        "آمار", default=list, blank=True,
        help_text='[{"en":"6","fa":"۶","label_en":"Years","label_fa":"سال"}, ...]'
    )
    skills = models.JSONField(
        "مهارت‌ها", default=list, blank=True,
        help_text='[{"en":"Python","fa":"پایتون","level":100}, ...]'
    )
    reviews = models.JSONField(
        "نظرات", default=list, blank=True,
        help_text='[{"name_en":"Sara","name_fa":"سارا","role_en":"...","role_fa":"...","text_en":"...","text_fa":"..."}, ...]'
    )
    project_options = models.JSONField(
        "گزینه‌های نوع پروژه", default=list, blank=True,
        help_text='["Software system", "AI solution", ...] (به هر دو زبان مشترک است یا می‌توانید dict بسازید)'
    )

    # ==== شبکه‌های اجتماعی (موجود) ====
    phone = models.CharField("شماره تماس", max_length=40, blank=True)
    email = models.EmailField("ایمیل", blank=True)
    linkedin = models.URLField("لینک لینکدین", blank=True)
    instagram = models.URLField("لینک اینستاگرام", blank=True)
    github = models.URLField("لینک گیت‌هاب", blank=True)
    telegram = models.URLField("لینک تلگرام", blank=True)

    class Meta:
        verbose_name = "تنظیمات و محتوای سایت"
        verbose_name_plural = "تنظیمات و محتوای سایت"

    def __str__(self):
        return "تنظیمات کلی سایت"

    @classmethod
    def load(cls):
        """همیشه یک رکورد برمی‌گرداند (اگر نبود، می‌سازد)."""
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj



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