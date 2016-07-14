from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^home', views.Home.as_view(), name='home'),
	url(r'^sen', views.sen, name='sen'),
	url(r'^cos', views.cos, name='cos'),
	url(r'^tan', views.tan, name='tan'),
]