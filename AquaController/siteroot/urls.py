from django.conf.urls import patterns, include, url
from siteroot import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='home'),
)