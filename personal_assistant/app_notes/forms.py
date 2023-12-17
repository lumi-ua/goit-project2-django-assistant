from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('name', 'description', 'done', 'tags',)
        widgets = {
            'tags': forms.CheckboxSelectMultiple,
        }
