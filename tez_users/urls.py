from django.conf.urls import patterns, url
from tez_users import views

urlpatterns = patterns('',
        url(r'^$', views.login, name='login'),
        url(r'^login/$', views.login, name='login'),
        url(r'^login/post$', views.login_post, name='login_post'),
        url(r'^logout/$', views.logout, name='logout'),
        url(r'^loggedin/$', views.loggedin, name='loggedin'),
        url(r'^ivalid/$', views.ivalid, name='ivalid'),
        url(r'^register/$', views.register, name='register'),
                       )
