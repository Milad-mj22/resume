from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.root_redirect, name="root"),
    path("contact/", views.contact, name="contact"),
    path("<str:lang>/", views.home, name="home"),
    path("<str:lang>/projects/<slug:slug>/", views.project_detail, name="project"),
    path("<str:lang>/blog/", views.blog_list, name="blog"),
    path("<str:lang>/blog/<slug:slug>/", views.blog_detail, name="post"),
    path("<str:lang>/projects/", views.projects_list, name="projects_list"),
]
