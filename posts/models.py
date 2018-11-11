from django.conf import settings
from django.db import models

from django.template.defaultfilters import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, related_name="created_by",
        on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}")

        super().save(*args, **kwargs)

class PostTexts(models.Model):
    text = models.CharField(max_length=2000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    version = models.IntegerField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, related_name="author",
        on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
