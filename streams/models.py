
from django.db import models
from django.contrib.auth.models import User 

class Stream(models.Model):
    stream_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=20, unique=True)
    stream_key = models.CharField(max_length=32)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.stream_name

    def generate_stream_key(self):
        """
        Uses Django's built-in make_random_password method to create
        a 21-character stream key
        """
        return User.objects.make_random_password(length=21)
