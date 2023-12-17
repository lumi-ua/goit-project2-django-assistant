from django.urls import path
from . import views

app_name = 'app_notes'

urlpatterns = [
    path('', views.main, name='main'),
    path('detail/<int:note_id>/', views.detail, name='detail'),
    path('note/', views.note, name='note'),
    path('tag/', views.tag, name='tag'),
    path('done/<int:note_id>/', views.set_done, name='set_done'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('search_note/', views.search_note, name='search_note'),
]
