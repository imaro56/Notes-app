from django import forms
from . import models


class CreateNote(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ['title', 'body']