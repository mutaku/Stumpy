from django.conf.urls.defaults import patterns, include, url

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
    
    # show the index from /
    url(r'^$', 'shortener.views.index'),
    # get a url for redirection /shorty
    url(r'^(?P<short>\w+)/$', 'shortener.views.detail'),
    # send a url to be shortened from /url/someencodedurl
    url(r'^url/(?P<stump>\S+)/$', 'shortener.views.submit'),

)
