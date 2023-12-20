from django.contrib import admin
from django.urls import path
from . import views


app_name = "app_download"

urlpatterns = [
    path("", views.main, name='files_browser'),
    path("upload/", views.upload, name='upload'),
    path("files/", views.files, name='files'),
    path("photo/", views.photo, name='photo'),
    path("music/", views.music, name='music'),
    path("video/", views.video, name='video'),
    path("other/", views.other, name='other'),
]