from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tezaurs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'website.views.home', name='home'),
    url(r'^website/', include('website.urls')),
    url(r'^inflect/', include('inflect.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
