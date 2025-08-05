from django import forms
from . import models


class CreateNote(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ['title', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title','autofocus': True, 'required': False}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your note'}),
        }