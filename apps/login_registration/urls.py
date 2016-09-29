from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.login_registration, name='login_registration'),
	url(r'^login$', views.login, name='login'),
	url(r'^process$', views.process, name='process'),
	url(r'^logout$', views.logout, name="logout"),
  ]