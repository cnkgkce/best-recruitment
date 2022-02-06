from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Candidate(models.Model):
    username = models.CharField(max_length=100)
    avatar_url = models.CharField(max_length=100)
    profile_url = models.CharField(max_length=100)
    email = models.CharField(null=True,max_length=100)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    repos = models.CharField(max_length=20)
  

    def __str__(self) -> str:
        return self.username


