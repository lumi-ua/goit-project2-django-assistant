from django.urls import path
from . import views

app_name = 'app_contacts'

urlpatterns = [    
    path('contact', views.contact, name='contact'),
    path('all-contacts', views.contacts, name='all_contacts'),
    path('upcoming-birthdays', views.upcoming_birthdays, name='upcoming_birthdays'),
    path('search-contacts', views.search_contacts, name='search_contacts'),
    path('edit-contact/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('delete-contact/<int:pk>/', views.delete_contact, name='delete_contact'),
]
