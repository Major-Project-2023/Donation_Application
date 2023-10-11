from django.contrib import admin
from .models import(
    Customer,
    Transaction,
    Miner,
    NGO,
)
# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','phone','address','country','ac_number','ifsc_code']

@admin.register(Transaction)
class TransactionModelAdmin(admin.ModelAdmin):
    list_display = ['id','sender','reciver','date','amount','currency','mode_of_payment']

@admin.register(Miner)
class MinerModelAdmin(admin.ModelAdmin):
    list_display = ['id','ip_address','country']

@admin.register(NGO)
class NGOModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','registration_number','contact_person','email','phone_number','address','country','mission_statement','website','bank_account_number','social_media_links','registration_proof','created_at']