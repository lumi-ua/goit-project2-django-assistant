from django.forms import ModelForm, TextInput, FileInput, CharField, FileField

from .models import File

class FileForm(ModelForm):
    description = CharField(max_length=150, required=False, widget=TextInput(attrs={"class": "form-control"}))
    path = FileField(widget=FileInput(attrs={"class": "form-control"}))
    
    class Meta:
        model = File
        fields = ['description', 'path']