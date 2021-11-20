from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import date
from django.core.exceptions import ValidationError
from django.conf import settings
from django.http import request

# Create your models here.

def upload_location(instance, filename):
    today = date.today()
    *filebase, extension = filename.split('.')
    title = str(instance.name)
    title = title.split(' ')
    title = '-'.join(title)
    title = title.split('.')
    title = ('-'.join(title)).lower()
    id = uuid.uuid4()
    new_file_name = title+'-'+str(id)+'-'+'.'+extension
    return 'category/'+today.strftime('%Y')+'/'+today.strftime('%m')+'/'+today.strftime('%d')+'/'+new_file_name

def validate_name(value):
    if len(value) <= 3:
        raise ValidationError('Masa cuman '+value+' doang?')
    return value

DEFAULT = 'category/category.png'

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, validators=[validate_name])
    description = models.CharField(max_length=255,null=True, blank=True)
    status = models.BooleanField(default=True, blank=True)
    # image = models.ImageField(upload_to=upload_location, default='category/category.png', null=True, blank=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='+', on_delete=models.SET_NULL, null=True, editable=False)
    updated_by = models.ForeignKey(User, related_name='+', on_delete=models.SET_NULL, null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
       
    class Meta:
        ordering = ['name','-created_at']

    def __str__(self):
        return self.name

    # def created_by(self, id):
    #     self.created_by = id

    # def save(self, userId=None):
    #     self.created_by = userId 
    #     print(self.created_by)
    #     if len(self.description) < 3:
    #         self.description = 'Kurang dari 3 nih'
        # if self._state.adding:
        #     self.created_by = self.
        # else:              
        #     self.updated_by = request.user.id
        # super().save()

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
    
    # def set_image_to_default(self):
    #     self.image.delete(save=False)  # delete old image file
    #     self.image = DEFAULT
    #     self.save()