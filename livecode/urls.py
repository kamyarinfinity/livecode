from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'liveview.views.home', name='home'),
    url(r'^oracle/$', 'liveview.views.oracle', name='oracle'),
    url(r'^raw/(?P<type>html|css|js)/$', 'liveview.views.raw_view', name='raw_view'),
    url(r'^post/(?P<type>html|css|js)/$', 'liveview.views.post_view', name='post_view'),
    url(r'^liveview/$', 'liveview.views.liveview', name='live_view'),

    url(r'^admin/', include(admin.site.urls)),
)
