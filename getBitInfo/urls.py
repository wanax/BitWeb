from django.conf.urls import patterns, url

from getBitInfo  import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index')
)
