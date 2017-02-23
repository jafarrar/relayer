
from django.conf.urls import url

from . import views

app_name = 'streams'
urlpatterns = [
    # ex: /
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /settings/
    url(r'^settings/$', views.SettingsView.as_view(), name='settings'),
    # ex: /settings/generate_stream_key
    url(r'^settings/generate_stream_key', views.generate_stream_key_view,
        name='generate_steam_key'),
    # ex: /billy/
    url(r'^(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name='detail'),
]
