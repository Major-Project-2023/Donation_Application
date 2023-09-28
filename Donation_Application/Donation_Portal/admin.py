from django.contrib import admin
from .models import(
    userSignup,

)
# Register your models here.
@admin.register(userSignup)
class userSignupModelAdmin(admin.ModelAdmin):
    list_display = ['id','email','password','phone','country']
