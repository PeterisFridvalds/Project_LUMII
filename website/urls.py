from django.conf.urls import patterns, url
from website import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^show/', views.redirect_to_show, name='redirect_to_show'),
        url(r'^(?P<input_word>\w+)/(?P<word_ID>[0-9]+)', views.show_word, name='show_word'),
                       )
