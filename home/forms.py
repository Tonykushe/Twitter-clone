from django import forms
from home.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class EditProfileForm(UserChangeForm):

	class Meta:
		model = User
		fields = (

			'first_name',
			'last_name',
			'email',
			'password'

		)


class HomeForm(forms.ModelForm):
	post = forms.CharField()

	class Meta:
		model = Post
		fields = ('post',)	
