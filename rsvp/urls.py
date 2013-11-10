from django.conf.urls import patterns, url
from rsvp.forms import ContactForm, GuestAuth, GuestVerify, GuestAttending, GuestNamesVerify

# Uncomment the next two lines to enable the admin:
urlpatterns = patterns('rsvp.views',
    # Examples:
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'yes/$', 'GuestVerifyView', name='GuestVerify'),
	url(r'contact/$', 'ContactView', name='ContactView'),
	url(r'request/$', 'RequestView', name='RequestView'),
	url(r'^$', 'GuestAuthView', name='GuestAuth'),

    # url(r'^(?P<string>\w+)/$', 'page', name='page'),
)
