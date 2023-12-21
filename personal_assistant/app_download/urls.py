from django.contrib import admin
from django.urls import path
from . import views


app_name = "app_download"

urlpatterns = [
    path("", views.main, name='files_browser'),
    path("upload/", views.upload, name='upload'),
    path("files/", views.files, name='files'),

    path("images/", views.images, name='image'),
    path("documents/", views.documents, name='document'),
    path("musics/", views.musics, name='music'),
    path("videos/", views.videos, name='video'),
    path("archives/", views.archives, name='archive'),
    path("others/", views.others, name='other'),

    path("delete-file/<int:f_id>", views.delete_file, name='delete_file'),
    path("edit-description/<int:f_id>", views.edit_description, name='edit_description'),
]
