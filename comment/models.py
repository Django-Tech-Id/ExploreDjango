from django.db import models
import uuid
from post.models import Post
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField(max_length=255)
    created_by = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE, null=True, editable=False)
    updated_by = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE, null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment