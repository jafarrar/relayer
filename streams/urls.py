from django.conf.urls import url

from . import views

app_name = 'streams'
urlpatterns = [
    # ex: /streams/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /streams/5/
    url(r'^(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name='detail'),
]
