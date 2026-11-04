"""
ساخت PDF از صفحه‌ی اصلی با مرورگر واقعی (Chromium / Playwright)
تا خروجی دقیقاً همان چیزی باشد که در مرورگر دیده می‌شود.

نصب (یک بار):
    pip install playwright
(دانلود مرورگر لازم نیست: از Microsoft Edge یا Google Chrome نصب‌شده روی سیستم استفاده می‌شود.
 اگر هیچ‌کدام نبود: python -m playwright install chromium
 یا مسیر مرورگر را در متغیر محیطی PDF_BROWSER_PATH بدهید.)
"""
import os
from urllib.parse import urlparse

VIEWPORT_W = 1280      # عرض صفحه‌ی PDF (پیکسل) — همان چیدمان دسکتاپ
VIEWPORT_H = 800       # ارتفاع هیرو در PDF (باید با --pdf-vh در CSS یکی باشد)


def _launch(p):
    """اول Edge، بعد Chrome نصب‌شده روی سیستم، در آخر Chromium خود Playwright."""
    path = os.environ.get("PDF_BROWSER_PATH")
    if path:
        try:
            return p.chromium.launch(executable_path=path)
        except Exception as e:
            raise RuntimeError(f"مرورگرِ مسیر PDF_BROWSER_PATH باز نشد: {path}\n{str(e).splitlines()[0]}")
    errors = []
    for channel in ("msedge", "chrome", None):
        try:
            return p.chromium.launch(channel=channel) if channel else p.chromium.launch()
        except Exception as e:                      # مرورگر نصب نیست → بعدی
            errors.append(f"{channel or 'chromium'}: {str(e).splitlines()[0]}")
    raise RuntimeError(
        "هیچ مرورگری پیدا نشد. Microsoft Edge یا Google Chrome را نصب کنید، "
        "یا مسیر آن را در متغیر محیطی PDF_BROWSER_PATH بگذارید.\n" + "\n".join(errors))


def render_pdf(url, cookies=None):
    from playwright.sync_api import sync_playwright

    origin = "{0.scheme}://{0.netloc}".format(urlparse(url))
    with sync_playwright() as p:
        browser = _launch(p)
        try:
            ctx = browser.new_context(viewport={"width": VIEWPORT_W, "height": VIEWPORT_H})
            if cookies:  # تم و زبان انتخابی کاربر (سشن) را به مرورگر می‌دهیم
                ctx.add_cookies([{"name": k, "value": v, "url": origin} for k, v in cookies.items()])
            page = ctx.new_page()
            page.goto(url, wait_until="networkidle", timeout=60_000)
            page.evaluate("document.fonts.ready")            # صبر برای فونت‌ها
            page.emulate_media(media="screen")               # همان استایل صفحه، نه استایل چاپ
            height = page.evaluate("Math.ceil(document.documentElement.scrollHeight)")
            return page.pdf(
                width=f"{VIEWPORT_W}px", height=f"{height + 2}px",   # یک صفحه‌ی پیوسته
                print_background=True, page_ranges="1",
                margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            )
        finally:
            browser.close()
