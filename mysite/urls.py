from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'tezaurs.views.home', name='home'),
    url(r'^tezaurs/', include('tezaurs.urls')),
    url(r'^inflect/', include('inflect.urls')),
    url(r'^user/', include('tez_users.urls')),
    url(r'^db/', include('tez_db.urls')),
)
