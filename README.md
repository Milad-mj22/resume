# سایت رزومه / Portfolio — Django

## اجرا
```bash
python -m venv venv
source venv/bin/activate        # ویندوز: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # برای دیدن پیام‌های فرم در /admin
python manage.py runserver
```
سایت: http://127.0.0.1:8000  (فارسی `/fa/` و انگلیسی `/en/`)

## شخصی‌سازی
- **متن‌ها، پروژه‌ها، نظرات، آمار:** `portfolio/content.py`
- **عکس خودتان:** فایل `portfolio/static/portfolio/img/profile.png` (بهتر است PNG بدون پس‌زمینه باشد)
- **رنگ‌ها و فونت‌ها:** متغیرهای ابتدای `portfolio/static/portfolio/css/style.css`
- **پیام‌های فرم تماس:** پنل ادمین → «پیام‌های تماس»

## مدیریت محتوا از پنل ادمین (`/admin`)
- **پروژه‌ها:** افزودن، ویرایش، تغییر ترتیب (ستون «ترتیب») و مخفی‌کردن (تیک «منتشر شده»). هر پروژه صفحه‌ی جزئیات خودش را دارد: `/fa/projects/<slug>/`
- **وبلاگ:** مقاله‌های دوزبانه با تصویر شاخص: `/fa/blog/`
- هر پاراگراف را با یک خط خالی جدا کنید.
- اگر متن فارسی یا انگلیسی خالی بماند، متن زبان دیگر نمایش داده می‌شود.
- تصویرها در پوشه‌ی `media/` ذخیره می‌شوند.
- پروژه‌ها و یک مقاله‌ی نمونه هنگام `migrate` خودکار ساخته می‌شوند؛ از پنل ادمین ویرایش یا حذفشان کنید.
