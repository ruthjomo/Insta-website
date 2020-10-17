from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.user',on_delete=method.CASCADE)
    image = ImageField(blank=True,null=True)
    caption = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption
    