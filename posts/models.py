from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe


class Post(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    image = models.ImageField(upload_to='media')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title
