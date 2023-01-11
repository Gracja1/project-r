from django import forms
from . import models


class CreateComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['users', 'restaurant', 'text',]
