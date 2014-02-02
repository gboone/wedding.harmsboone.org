from django.conf.urls import patterns, url
from rsvp.forms import GuestAuth, GuestForm, GuestAttending, GuestChoice, PartyChoice
from posts.models import Post
# Uncomment the next two lines to enable the admin:
urlpatterns = patterns('rsvp.views',
    # Examples:
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^$', 'GuestAuthView', name='GuestAuth'),
	url(r'attending/$', 'GuestAttendanceView', name='GuestAttending'),
	url(r'yes/$', 'GuestVerifyView', name='GuestVerify'),
	url(r'request/$', 'RequestView', name='RequestView'),
	url(r'confirm/$', 'GuestConfirmView', name='Confirm'),
	url(r'reports/$', 'ReportView', name='ReportView'),

    # url(r'^(?P<string>\w+)/$', 'page', name='page'),
)
