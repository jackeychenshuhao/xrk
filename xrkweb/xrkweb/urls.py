from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from jackey.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xrkweb.views.home', name='home'),
    # url(r'^xrkweb/', include('xrkweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
	(r'^$', index),
	(r'xrk_login/$', xrk_login),
	(r'xrk_errlogin/$', xrk_errlogin),
	(r'^logout/$', logout),
	(r'^config_center/$', config_center),
	(r'^admin_center/$', admin_center),
	(r'^moniter_center/$', moniter_center),
	(r'^rsync_center/$', rsync_center),
    (r'^getmemory/$',getmemory),
    (r'^command_center/$',command_center),
)
