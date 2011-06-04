from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Stumpy.views.home', name='home'),
    # url(r'^Stumpy/', include('Stumpy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
 
    # logging in and out handlers
    (r'^accounts/login/$',  'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    
    # show the index from /
    url(r'^$', 'shortener.views.index'),
    # iframer bookmarklet
    url(r'^iframer/$', 'shortener.views.iframer'),
    # get a url for redirection /shorty
    url(r'^(?P<short>[0-9a-zA-Z]+)/$', 'shortener.views.detail'),
    # send a url to be shortened from /url/someencodedurl
    url(r'^url/(?P<stumpurl>\S+)/$', 'shortener.views.submit'),

)
