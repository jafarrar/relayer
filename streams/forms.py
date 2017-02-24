
from django.forms import ModelForm
from .models import Stream

class StreamForm(ModelForm):
    class Meta:
        model = Stream
        fields = ['stream_name', 'stream_key', 'description', 'is_private']
        labels = {
            'stream_name': ('Stream Title'),
            'stream_key': ('Stream Key'),
            'is_private': ('Private'),
        }
