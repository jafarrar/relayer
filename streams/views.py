
from django.utils import timezone
from django.views import generic
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import Stream

class IndexView(generic.ListView):
    """
    Defines the index view that lists 20 streams
    """
    template_name = 'streams/index.html'
    context_object_name = 'latest_stream_list'

    def get_queryset(self):
        """
        Return the last 20 streams created.
        """
        if self.request.user.is_staff:
            return Stream.objects.filter(
                creation_date__lte=timezone.now()
            ).order_by('-creation_date')[:20]
        else:
            return Stream.objects.filter(
                creation_date__lte=timezone.now(),
                is_private=False
            ).order_by('-creation_date')[:20]

class DetailView(generic.DetailView):
    """
    Defines the view for a single stream
    """
    model = Stream
    template_name = 'streams/detail.html'

class SettingsView(generic.DetailView):
    """
    Defines the view for a single stream
    """
    model = Stream
    template_name = 'streams/settings.html'
