
from django.utils import timezone
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from .helpers import generate_stream_key
from .models import Stream

class IndexView(generic.ListView):
    """
    Defines the index view that lists 20 streams
    """
    template_name = 'streams/index.html'
    context_object_name = 'latest_stream_list'

    def get_queryset(self):
        """
        Return the last 20 streams created, excluding private streams unless >staff
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


class SettingsView(LoginRequiredMixin, generic.UpdateView):
    """
    Defines the view for a user's settings page
    """
    model = Stream
    fields = ['stream_name', 'description', 'stream_key', 'is_private']
    template_name = 'streams/settings.html'

    login_url = '/login/'
    success_url = '/settings' #placeholder while I wrangle with reverse/reverse_lazy

    def get_object(self, queryset=None):
        return Stream.objects.get(slug=self.request.user.stream.slug)

def generate_stream_key_view(request):
    return JsonResponse({'key': generate_stream_key()})
