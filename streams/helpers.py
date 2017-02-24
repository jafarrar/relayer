
from django.contrib.auth.models import User

def generate_stream_key():
    """
    Uses Django's built-in make_random_password method to create
    a 21-character stream key
    """
    return User.objects.make_random_password(length=21)
