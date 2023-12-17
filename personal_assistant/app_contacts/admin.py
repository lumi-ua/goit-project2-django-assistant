from django.contrib import admin

from .models import Contact, EmailAddress, PhoneNumber

# Register your models here.

admin.site.register(Contact)
admin.site.register(EmailAddress)
admin.site.register(PhoneNumber)
