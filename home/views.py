from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from home.forms import *
from home.models import *
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
class HomeView(TemplateView):
	template_name = 'home/home.html'

	def get(self, request):
		form = HomeForm()
		posts = Post.objects.all().order_by('-created')
		users = User.objects.exclude(id=request.user.id)

		args = {'form': form, 'posts': posts, 'users': users}
		return render(request, self.template_name, args)

	def post(self, request):
		form = HomeForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()

			text = form.cleaned_data['post']
			form = HomeForm()
			return redirect('home:home')

		args = {'form': form, 'text': text}
		return render(request, self.template_name, args)



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

