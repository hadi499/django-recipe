from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='media/img')

    def __str__(self):
        return self.title
