from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from mysite.models import Post
from rsvp.models import *
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'mysite.views.index'),
    url(r'^(?P<string>\w+)/$', 'mysite.views.page'),
)
