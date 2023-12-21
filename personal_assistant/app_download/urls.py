from django.contrib import admin
from django.urls import path
from . import views


app_name = "app_download"

urlpatterns = [
    path("", views.main, name='files_browser'),
    path("upload/", views.upload, name='upload'),
    path("files/", views.files, name='files'),

    path("images/", views.images, name='images'),
    path("documents/", views.documents, name='documents'),
    path("musics/", views.musics, name='musics'),
    path("videos/", views.videos, name='videos'),
    path("archives/", views.archives, name='archives'),
    path("others/", views.others, name='others'),

    path("delete-file/<int:f_id>", views.delete_file, name='delete_file'),
    path("edit-description/<int:f_id>", views.edit_description, name='edit_description'),
]
