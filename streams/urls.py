
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'streams'
urlpatterns = [
    # ex: /
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /settings
    url(r'^settings/$', views.SettingsView.as_view(), name='settings'),
    # ex: /billy/
    url(r'^(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name='detail'),
]