from django.conf import settings


def theme(request):
    """نام تم آماده (SITE_THEME در settings.py) را به همه‌ی قالب‌ها می‌دهد."""
    return {"theme": getattr(settings, "SITE_THEME", "")}
