from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField(default='', blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title