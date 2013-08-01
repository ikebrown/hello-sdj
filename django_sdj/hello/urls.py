from django.conf.urls import patterns, url

from hello import views

urlpatterns = patterns(
    '',
    url(r'^hello$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^thanks$', views.thanks, name='thanks'),
    url(r'^messages$', views.messages, name='messages'),
)
