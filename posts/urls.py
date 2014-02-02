from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
urlpatterns = patterns('posts.views',
    # Examples:
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^$', 'index', name='home'),
	url(r'thanks/', 'thanks', name='thanks'),
    url(r'^(?P<string>\w+)/$', 'page', name='page'),
)
