from django.forms import ModelForm, CharField, EmailField, DateField
from phonenumber_field.formfields import PhoneNumberField
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import Contact, PhoneNumber, EmailAddress




class ContactForm(ModelForm):
    fullname = CharField(max_length=255, 
        widget=forms.TextInput(attrs={'placeholder': 'Name Lastname', "class": "form-control"}))
    address = CharField(max_length=255, required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'City, Street, House number', "class": "form-control"}))
    birthday = DateField(required=False, input_formats=["%d.%m.%Y"], 
        widget=forms.DateInput(attrs={'placeholder': 'DD.MM.YYYY', 'class': 'form-control'}))
    class Meta:
        model = Contact
        fields = ["fullname", "address", "birthday"]
        exclude = ["user"]

    

class PhoneNumberForm(forms.ModelForm):
        phone_number = PhoneNumberField(
            widget=PhoneNumberPrefixWidget(attrs={'placeholder': '+380', 'class': 'form-control'})
        )
        class Meta:
            model = PhoneNumber
            fields = ["phone_number"]
            exclude = ["contact"]

class EmailAddressForm(forms.ModelForm):
        email = EmailField(max_length=100, required=False, widget=forms.EmailInput(attrs={'placeholder': 'example@email.com', 'class': 'form-control'}))

        class Meta:
            model = EmailAddress
            fields = ["email"]
            exclude = ["contact"]
