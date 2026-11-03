from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.root_redirect, name="root"),
    path("contact/", views.contact, name="contact"),
    
    # آدرس‌های مربوط به پروژه‌ها
    path("<str:lang>/projects/", views.projects_list, name="projects_list"),
    path("<str:lang>/projects/<slug:slug>/", views.project_detail, name="project"),
    
    # آدرس‌های مربوط به وبلاگ
    path("<str:lang>/blog/", views.blog_list, name="blog"),
    path("<str:lang>/blog/<slug:slug>/", views.blog_detail, name="post"),
    
    # آدرس صفحه اصلی (باید آخر باشد تا با بقیه تداخل نکند)
    path("<str:lang>/", views.home, name="home"),
]