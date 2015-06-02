from django.conf.urls import patterns, url
from tez_db import views

urlpatterns = patterns('',
        url(r'^$', views.db, name='db'),
        url(r'^create_db/$', views.create_db, name='create_db'),
        url(r'^add_db_object/$', views.add_db_object, name='add_db_object'),
        url(r'^add_correction/(?P<word>\w+)/(?P<word_ID>[0-9]+)', views.add_correction, name='add_correction'),
        url(r'^show_corrections/$', views.show_corrections, name='show_corrections'),
        url(r'^redirect_to/$', views.redirect_to, name='redirect_to'),
        url(r'^show_json/(?P<word>\w+)/(?P<word_ID>[0-9]+)', views.show_json, name='show_json'),
        url(r'^update_db_object/(?P<word>\w+)/(?P<word_ID>[0-9]+)', views.update_db_object, name='update_db_object'),
                       )
