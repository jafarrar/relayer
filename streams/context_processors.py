
from django.conf import settings


def global_settings(request):
    # return any necessary values
    return {
        'RTMP_BASE_URL': settings.RTMP_BASE_URL,
        'JWPLAYER_KEY': settings.JWPLAYER_KEY
    }
    