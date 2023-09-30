from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    ac_number = models.IntegerField(unique=True)
    ifsc_code = models.CharField(max_length=11)
    def __str__(self):
        return str(self.id)