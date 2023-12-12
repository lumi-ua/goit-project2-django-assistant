from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Contact(models.Model):
    fullname = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = PhoneNumberField(blank=False)
    email = models.EmailField(unique=True)
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.fullname} ({self.phone_number})"
