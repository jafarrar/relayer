
from .models import Stream

from django.test import TestCase
from django.urls import reverse

def create_stream(stream_name, slug, is_private):
    """
    Creates a stream with the given name, slug, and private status.
    """
    return Stream.objects.create(stream_name=stream_name, slug=slug, is_private=is_private)

class StreamMethodTests(TestCase):
    def test_generated_stream_key_is_to_specs(self):
        """
        generate_stream_key() should a generate a 21-character string
        """
        stream = Stream(stream_name='test stream')
        stream.stream_key = stream.generate_stream_key()
        self.assertEqual(len(stream.stream_key), 21)

class StreamIndexTests(TestCase):
    def test_index_view_with_no_streams(self):
        """
        If no streams exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('streams:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No streams are available.")
        self.assertQuerysetEqual(response.context['latest_stream_list'], [])

class StreamViewTests(TestCase):
    def test_detail_view_is_empty_if_private(self):
        """
        If the stream is prviate, user should not see anything.
        """
        private_stream = create_stream(stream_name='hidden stream',
                                       slug='hiddenstream', is_private=True)

        url = reverse('streams:detail', args=(private_stream.slug,))
        response = self.client.get(url)
        self.assertContains(response, "Private stream.")
