from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


# Managers
class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='2').order_by('-publish')


class Article(models.Model):
    STATUS_CHOICES = [
        ('1', 'Deraft'),
        ('2', 'Publish'),
        ]
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, allow_unicode=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextUploadingField()
    publish= models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1')
    objects = models.Manager()
    publish_objects = PublishManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post_detail', args=(self.id, self.slug))
