from django import forms
from .models import Note


class NoteForms(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('name', 'description', 'done', 'tags',)
        widgets = {
            'tags': forms.CheckboxSelectMultiple,
        }
