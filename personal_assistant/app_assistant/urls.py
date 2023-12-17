from django.urls import path
from . import views
from django.contrib import admin
app_name = 'app_assistant'

urlpatterns = [

    path('', views.main, name='main'),
    path("admin/", admin.site.urls),

]