from django import forms
from .models import UploadedFile
from django.forms import ModelForm, ImageField, CharField, FileInput, TextInput
from .models import Picture

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']


class PictureForm(ModelForm):
    description = CharField(max_length=150, widget=TextInput(attrs={"class": "form-control"}))
    path = ImageField(widget=FileInput(attrs={"class": "form-control"}))

    class Meta:
        model = Picture
        fields = ['description', 'path']
