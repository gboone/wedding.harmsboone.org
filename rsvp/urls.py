from django.conf.urls import patterns, url
from rsvp.forms import ContactForm

# Uncomment the next two lines to enable the admin:
urlpatterns = patterns('rsvp.views',
    # Examples:
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'contact/$', 'ContactView', name='ContactView'),
	url(r'request/$', 'RequestView', name='RequestView'),
    # url(r'^(?P<string>\w+)/$', 'page', name='page'),
)
