from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

    # Post :
    #   - title
    #   - author
    #   - createed_at
    #   - content

class Post(models.Model):  # db table
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    createed_at = models.DateTimeField(default=timezone.now)
    post_slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='post/')
    active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        #logic
        self.post_slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title