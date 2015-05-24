from django.conf.urls import patterns, url
from tezaurs import views

urlpatterns = patterns('',
        url(r'^$', views.home, name='home'),
        url(r'^saglab_db/', views.add_to_db, name='add_to_db'),
        url(r'^show_db/', views.show, name='show'),
        url(r'^show/', views.redirect_to_show, name='redirect_to_show'),
        url(r'^(?P<input_word>\w+)/(?P<word_ID>[0-9]+)', views.show_word, name='show_word'),
                       )
