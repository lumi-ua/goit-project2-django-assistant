from django.forms import ModelForm, CharField, EmailField, DateField
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField
from phonenumbers import is_valid_number

from .models import Contact

class ContactForm(ModelForm):
    fullname = CharField(max_length=50, required=True)
    address = CharField(max_length=50, required=False)
    phone_number = PhoneNumberField(required=True)                               
    email = EmailField(max_length=25, required=True)
    birthday = DateField(required=False, input_formats=["%d.%m.%Y"])                        
                            

    class Meta:
        model = Contact
        fields = ["fullname", "address", "phone_number", "email", "birthday"]


    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]

        if not is_valid_number(phone_number):
            raise ValidationError("Incorrect phone number format")           

        return phone_number
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not '@' in email or '.' not in email.split('@')[-1]:
            raise ValidationError('Invalid email address.')
        return email
