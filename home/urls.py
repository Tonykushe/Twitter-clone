from django.conf.urls import url
from home.views import *

urlpatterns = [
	#url(r'^$', home, name='home'),
	url(r'^$', HomeView.as_view(), name='home'),
	url(r'myprofile/$', profile, name='profile'),
	url(r'myprofile/edit/$', editprofile, name='edit_profile'),
	url(r'change-password/$', change_password, name='edit_password'),
]


