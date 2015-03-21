from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('siteroot.urls', namespace="siteroot")),
    url(r'^admin/', include(admin.site.urls)),
)
