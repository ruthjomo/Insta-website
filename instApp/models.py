from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)

    

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Post(models.Model):
    author  = models.ForeignKey('auth.User',on_delete=models.CASCADE, related_name='posts')
    image   = models.ImageField(default='default.png',blank=True)
    caption = models.TextField()
    likes   = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')
    created_date = models.DateTimeField(default=timezone.now) 
   

class Profile(DetailView):
    template_name = 'profile.html'
    queryset = User.objects.all()
    

                 



