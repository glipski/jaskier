from django.conf.urls import url
from . import views

urlpatterns = [
   	url(r'^login/$', views.login_page),
	url(r'^registration/$', views.registration_page),
	url(r'^logout/$', views.logout_page),
	url(r'^$', views.index, name = 'index'),
]
