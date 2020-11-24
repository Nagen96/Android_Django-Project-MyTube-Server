from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Video(models.Model):
    title = models.TextField()
    content = models.TextField()
    video = models.TextField()
    thumbnail = models.TextField()


class User(AbstractUser):
    nickname = models.CharField(max_length=20)


class Comment(models.Model):
    token = models.CharField(max_length=20)
    comment_text = models.TextField()
