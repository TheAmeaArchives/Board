from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Curation(models.Model):
    user =models.ForeignKey(User, related_name='curator', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=225)
    sub_title = models.CharField(max_length=225)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Post(models.Model):
    USER_TYPE = (
        ('chief','Chief'),
        ('member','Member')
    )
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, choices=USER_TYPE, default="member")
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.title
