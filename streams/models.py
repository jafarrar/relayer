
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Stream(models.Model):
    """
    Defines the model of a stream or a "channel"
    that's owned by its creator
    """
    stream_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=20, unique=True)
    description = models.CharField(max_length=256, default='')
    stream_key = models.CharField(max_length=32)
    creation_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.stream_name

    def generate_stream_key(self):
        """
        Uses Django's built-in make_random_password method to create
        a 21-character stream key
        """
        return User.objects.make_random_password(length=21)
