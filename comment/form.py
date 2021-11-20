from django import forms
from django.forms import ModelForm, fields
from django.http import request
from .models import Comment
from django.utils.translation import ugettext_lazy as _
from urllib.parse import urlparse

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
        labels = {
            'comment': _('Nama'),
        }
        widgets = {
            'post': forms.HiddenInput(attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment'}),
        }