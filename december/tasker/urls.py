from django.conf.urls import patterns, include, url

from tasker import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<task_id>\d+)/$', views.detail, name='detail'),
	url(r'^(?P<task_id>\d+)/edit/$', views.edit, name='edit'),
	url(r'^new/$', views.new, name='new'),	
	url(r'^(?P<task_id>\d+)/delete/$', views.delete, name='new'),	
)