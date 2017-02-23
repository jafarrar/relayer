
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.dispatch import receiver
from django.db.models.signals import post_save

from .helpers import generate_stream_key

def generate_slug(stream_name):
    """
    Generates a slug based on stream_name
    """
    return slugify(stream_name)

class Stream(models.Model):
    """
    Defines the model of a stream or a "channel"
    that's owned by its creator
    """
    stream_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=20, unique=True)
    description = models.CharField(max_length=256, default='')
    stream_key = models.CharField(max_length=32, default=generate_stream_key)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.stream_name

    def get_absolute_url(self):
        return reverse_lazy('settings')

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_stream_for_new_user(sender, created, instance, **kwargs):
    """
    Creates a new Stream object with a one-to-one relationship when a user is created
    """
    if created:
        stream = Stream(
            user=instance,
            stream_name=instance.username,
            slug=generate_slug(instance.username))
        stream.save()
