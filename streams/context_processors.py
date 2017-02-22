
from django.conf import settings
from django.utils import timezone
from .models import Stream


def global_settings(request):
    """
    Makes the RTMP URL and JWPlayer key available in templates
    """
    return {
        'RTMP_BASE_URL': settings.RTMP_BASE_URL,
        'JWPLAYER_KEY': settings.JWPLAYER_KEY
    }

def nav_stream_list(request):
    """
    Makes the 5 most recent streams available to the navbar
    """
    if request.user.is_staff:
        streams = Stream.objects.filter(
            creation_date__lte=timezone.now()
        ).order_by('-creation_date')[:5]
    else:
        streams = Stream.objects.filter(
            creation_date__lte=timezone.now(),
            is_private=False
        ).order_by('-creation_date')[:5]

    return {
        'NAV_STREAM_LIST': streams
    }
