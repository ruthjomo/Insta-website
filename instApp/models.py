from django.db import models
from django.utils import timezone
from django.db.models import ImageField

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete = models.CASCADE)
    image = ImageField(blank=True,null=True)
    caption = models.TextField()
    location = models
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption
    