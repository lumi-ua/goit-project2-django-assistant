from django.urls import path
from . import views

app_name = 'app_assistant'

urlpatterns = [

path('', views.main, name='main'),

]