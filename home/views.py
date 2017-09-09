from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from home.forms import *
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	args = locals()

	return render(request, 'home/home.html', args)

@login_required
def profile(request, pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user = request.user

	args = {'user': user}
	return render(request, 'home/profile.html', args)

@login_required
def editprofile(request):
	if request.method =='POST':
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect(reverse('home:profile'))

	else:
		form = EditProfileForm(instance=request.user)
		args = {'form' : form}
		return render(request, 'home/editprofile.html', args)

def change_password(request):
	if request.method =='POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect(reverse('home:profile'))

		else:
			return redirect(reverse('home:change-password'))


	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form' : form}
		return render(request, 'home/editpassword.html', args)

