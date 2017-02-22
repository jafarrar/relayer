
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Stream

def create_stream(stream_name, slug, is_private):
    """
    Creates a stream with the given name, slug, and private status.
    """
    return Stream.objects.create(stream_name=stream_name, slug=slug, is_private=is_private)

def create_user(username, is_staff):
    """
    Create a user with the given parameters
    """
    password = User.objects.make_random_password(length=21)
    return User.objects.create_user(username=username, password=password, is_staff=is_staff)

class StreamMethodTests(TestCase):
    """
    Tests for the Stream model's methods
    """
    def test_generated_stream_key_is_to_specs(self):
        """
        generate_stream_key() should a generate a 21-character string
        """
        stream = Stream(stream_name='test stream')
        self.assertEqual(len(stream.stream_key), 21)

class StreamIndexTests(TestCase):
    """
    Tests for index.html
    """
    def test_index_view_with_no_streams(self):
        """
        If no streams exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('streams:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No streams are available.")
        self.assertQuerysetEqual(response.context['latest_stream_list'], [])

    def test_index_view_hides_private_streams(self):
        """
        If the user is logged in, private streams will not show
        """
        private_stream = create_stream(stream_name='hidden stream',
                                       slug='hiddenstream', is_private=True)
        response = self.client.get(reverse('streams:index'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_stream_list'], [])

class StreamViewTests(TestCase):
    """
    Tests for detail.html
    """
    def test_detail_view_is_empty_if_private(self):
        """
        If the stream is prviate, user should not see anything.
        """
        private_stream = create_stream(stream_name='hidden stream',
                                       slug='hiddenstream', is_private=True)

        url = reverse('streams:detail', args=(private_stream.slug,))
        response = self.client.get(url)
        self.assertContains(response, "Private stream!")
