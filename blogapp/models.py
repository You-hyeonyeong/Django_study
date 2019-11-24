from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10)
    userId = models.CharField(max_length=10)
    userPw = models.CharField(max_length=10)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()