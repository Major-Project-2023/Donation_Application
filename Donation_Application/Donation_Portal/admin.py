from django.contrib import admin
from .models import(
    Customer,
    Transaction,
    Miner
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