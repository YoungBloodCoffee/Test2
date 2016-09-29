from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^add_quote$', views.add_quote, name='add_quote'),
	url(r'^users/(?P<id>\d+)$', views.users, name='users'),
	url(r'^add_favorites$', views.add_favorites, name="add_favorites")
  ]