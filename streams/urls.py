
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'streams'
urlpatterns = [
    # ex: /streams/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /streams/billy/
    url(r'^(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /streams/billy/settings
    url(r'^(?P<slug>[-\w]+)/settings/$', views.SettingsView.as_view(), name='settings'),
]