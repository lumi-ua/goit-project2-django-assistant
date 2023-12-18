from django.urls import path
from . import views

app_name = 'app_contacts'

urlpatterns = [ 
    path('dashboard', views.dashboard, name='dashboard'),   
    path('contact', views.contact, name='contact'),
    path('all-contacts', views.contacts, name='all_contacts'),
    path("<int:page>", views.contacts, name="main_paginate"), 
    path('upcoming-birthdays', views.upcoming_birthdays, name='upcoming_birthdays'),
    path("<int:page>", views.upcoming_birthdays, name="upcoming_birthdays_paginate"),
    path('search-contacts', views.search_contacts, name='search_contacts'),
    path('edit-contact/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('delete-contact/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('add-phone-number/<int:pk>/', views.add_phone_number, name='add_phone_number'),
    path('add-email-address/<int:pk>/', views.add_email_address, name='add_email_address'),
    path('delete-phone/<int:pk>/', views.delete_phone, name='delete_phone'),
    path('delete-email/<int:pk>/', views.delete_email, name='delete_email'),
    
]
