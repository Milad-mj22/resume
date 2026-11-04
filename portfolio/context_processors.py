from django.conf import settings

def theme(request):
    """تم انتخابی کاربر را از سشن می‌خواند؛ در غیر این صورت از settings."""
    default = getattr(settings, "SITE_THEME", "ocean")
    current = request.session.get("theme", default)
    from .content import THEMES
    valid = {t["key"] for t in THEMES}
    if current not in valid:
        current = default
    return {"theme": current}