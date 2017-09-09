from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save 

# Create your models here.
class UserProfile(models.Model):
	user 		= models.OneToOneField(User)
	first_name  = models.CharField(max_length=100, default='')
	last_name   = models.CharField(max_length=100, default='')
	about       = models.CharField(max_length=100, default='')
	city 		= models.CharField(max_length=100, default='')
	website     = models.URLField(default='')
	phone		= models.IntegerField(default=0)
	profile_image  = models.ImageField(upload_to='profile_image', blank=True)	
	cover_image    = models.ImageField(upload_to='cover_image', blank=True)	

	def __str__(self):
		return self.user.username

class Post(models.Model):
	post = models.CharField(max_length=500)
	user = models.ForeignKey(User)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
class Friend(models.Model):
	users = models.ManyToManyField(User)

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
	

 