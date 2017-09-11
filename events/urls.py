from django.conf.urls import patterns, include, url



from events import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^logout/$', views.logout_view),
    url(r'^login/$',views.login_view),
    url(r'^signup/$',views.signup),
    url(r'^events/([0-9]+)/$',views.events),
    url(r'^attend/([0-9]+)/$',views.attend),
    url(r'^buy/([0-9]+)/$',views.buy),   
)