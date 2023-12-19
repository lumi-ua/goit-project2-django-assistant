from django.urls import path
from . import views

app_name = 'app_news'

urlpatterns = [
    path('', views.main, name='form_news'),
    path('news/', views.get_news, name='news'),
    path('sport/', views.get_sport_news, name='sport'),
    path('currency/', views.get_currency, name='currency'),
    path('weather/', views.get_weather, name='weather'),
]
