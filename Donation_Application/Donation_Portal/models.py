from django.db import models

# Create your models here.
class userSignup(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    phone = models.IntegerField()
    country = models.CharField(max_length=20)
 
