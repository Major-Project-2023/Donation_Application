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
        
    
class Transaction(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    reciver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciver')
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    currency = models.CharField(max_length=20)
    mode_of_payment = models.CharField(max_length=20)

class Miner(models.Model):
    ip_address = models.CharField(max_length=15)
    country = models.CharField(max_length=20)

class NGO(models.Model):
    name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    country = models.CharField(max_length=50)
    mission_statement = models.TextField()
    website = models.URLField(blank=True, null=True)
    bank_account_number = models.CharField(max_length=30)
    # projects_description = models.TextField()
    social_media_links = models.URLField(blank=True, null=True)
    registration_proof = models.ImageField(upload_to='media/static/images/')
    # accepted_terms = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name