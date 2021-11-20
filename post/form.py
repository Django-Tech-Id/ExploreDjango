from django import forms
from django.forms import ModelForm, fields
from .models import Post
from django.utils.translation import ugettext_lazy as _

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'category': _('Kategori'),
            'title': _('Title'),
            'summary': _('Summary'),
            'content': _('Kontent'),
            'image': _('Gambar'),
            'description': _('Deskripsi'),
            'status': _('Aktif'),
            'image': _('Gambar')
        }
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control col-md-12', 'placeholder': 'Name'}),
            'title': forms.TextInput(attrs={'class': 'form-control col-md-12', 'placeholder': 'Name'}),
            'summary': forms.TextInput(attrs={'class': 'form-control col-md-12', 'placeholder': 'Name'}),
            'content': forms.Textarea(attrs={'class': 'form-control col-md-12', 'placeholder': 'Name'}),
            'image': forms.FileInput(attrs={'class': 'form-control col-md-12'}),
            'description': forms.TextInput(attrs={'class': 'form-control col-md-12', 'placeholder': 'Description'}),
            'status': forms.Select(attrs={'class': 'form-control col-md-12'}),
            'publish_on': forms.DateInput(attrs={'type': 'date', 'class': 'form-control col-md-12'}),
        }

    # Agar Gambar hanya required saat create new form saja, dan not required saat edit
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        if self.initial:
            self.fields['image'].required = False