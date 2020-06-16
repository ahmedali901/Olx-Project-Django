from django.db import models
from django.utils import timezone

# Create your models here.

    # Post :
    #   - title
    #   - author
    #   - createed_at
    #   - content

class Post(models.Model):  # db table
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    createed_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title