from django.contrib import admin
from .models import(
    Customer,

)
# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','phone','address','country','ac_number','ifsc_code']
