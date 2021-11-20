import uuid
from django.db import models
from django.db.models.deletion import SET_NULL
from category.models import Category
from django.contrib.auth.models import User
from datetime import date
from django.core.exceptions import ValidationError
from django.conf import settings

# Create your models here.

def upload_location(instance, filename):
    today = date.today()
    *filebase, extension = filename.split('.')
    title = str(instance.title)
    title = title.split(' ')
    title = '-'.join(title)
    title = title.split('.')
    title = ('-'.join(title)).lower()
    id = uuid.uuid4()
    new_file_name = title+'-'+str(id)+'-'+'.'+extension
    return 'post/'+today.strftime('%Y')+'/'+today.strftime('%m')+'/'+today.strftime('%d')+'/'+new_file_name

def validate_name(value):
    if len(value) <= 3:
        raise ValidationError('Masa cuman '+value+' doang?')
    return value

class Post(models.Model):
    STATUS_CHOICE = (
        ('Draft', 'Draft'),
        ('Publish', 'Publish')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.PROTECT)
    title = models.CharField(max_length=50, validators=[validate_name])
    summary = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_location, default='post/post.jpg', null=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='Publish')
    publish_on = models.DateField(editable=True, null=False)
    created_by = models.ForeignKey(User, related_name='+', on_delete=models.SET_NULL, null=True, editable=False)
    updated_by = models.ForeignKey(User, related_name='+', on_delete=models.SET_NULL, null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self):
        if len(self.title) < 3:
            self.title = 'Kurang dari 3 nih'
        super().save()

    def delete(self):
        # Agar gambar default tidak bisa dihapus, ini belum jalan, gambar default masih bisa dihapus
        # https://stackoverflow.com/questions/70012552/prevent-default-image-deletion-django
        if self.image != 'category/category.png':
            print('Ini Isinya 1')
            print(self.image)
            print('Ini Isinya 2')
            self.image.delete()
        else:
            print('Ini Isinya 3')
            print(self.image)
            print('Ini Isinya 4')

        # super().delete(save=False)
        super().delete()
