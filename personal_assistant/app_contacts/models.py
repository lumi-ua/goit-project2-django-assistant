from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your models here.


class Contact(models.Model):
    fullname = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    

class EmailAddress(models.Model):
    email = models.EmailField(max_length=100, null=True)
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, default=None, null=True, related_name='email_addresses'
    )

    
   
class PhoneNumber(models.Model):
    phone_number = PhoneNumberField(null=True,)
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, default=None, null=True, related_name='phone_numbers'
    )

    
