# from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from .models import Customer, Transaction,NGO
from .forms import SignupForm ,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse
# from .models import Transaction

def home(request):
    all_ngos = NGO.objects.all()
    return render(request, 'home.html',{'ngos': all_ngos}) #{'navbar':'home'}
    # host = request.get_host()
    # paypal_checkout = {
    #     'business':settings.PAYPAL_RECEIVER_EMAIL,
    #     'donation_amount': Transaction.amount,
    #     'invoice' : uuid.uuid4(),
    #     'currency_code' : 'USD',
    #     'notify_url':f"https://{host}{reverse('paypal-ipn')}"
    # }
# class home(View):
#     def get(self,request):
#         ngo = NGO.objects.filter(name=request.name)
#         return render(request,'home.html',{'ngo':'ngo'})
    
@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        proff = Customer.objects.filter(user=request.user)
        form = CustomerProfileForm()
        return render(request,'profile.html',{'form':form,'proff':proff,'active':'btn-primary'})
 
    def post(self,request):
        form = CustomerProfileForm(request.POST) 
        proff = Customer.objects.filter(user=request.user)
        if form.is_valid(): 
            user = request.user
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            country = form.cleaned_data['country']
            ac_number = form.cleaned_data['ac_number']
            ifsc_code = form.cleaned_data['ifsc_code']
            reg = Customer(user=user,phone=phone,address=address,country=country,ac_number=ac_number,ifsc_code=ifsc_code)
            reg.save()
            messages.success(request,'Congratulations!! ProfileUpdated Successfully')
            return render(request,'profile.html',{'form':form,'proff':proff,'active':'btn-primary'})
        else:
            messages.MessageFailure(request,'Oh! No! ProfileUpdate Was Un-Successful')
            return render(request,'profile.html',{'form':form,'proff':proff,'active':'btn-primary'})
    
    def update(self,request):
        pass
    
    def delete(self,request):
        pass


def portal(request):
    ngo_id = request.GET.get('ngo_id')
    # ngo = get_object(NGO, id=ngo_id)
    return render(request, 'paymentportal.html', {'ngo_id': ngo_id}) 
    # {'navbar':'portal'},

class SignupView(View):
    def get(self,request):
        form = SignupForm()
        return render(request,'signup.html',{'form':form})
    def post(self,request):
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! Registered Successfully')
            form.save()
        return render(request,'signup.html',{'form':form})
 
# @login_required
# def address(request):
#     add = Customer.objects.filter(user=request.user)
#     return render(request, 'pro.html',{'add':add,'active':'btn-primary'})


@method_decorator(login_required,name='dispatch')
class TransactionView(View):
    def get(self,request):
        trans = Transaction.objects.filter(sender=request.user)
        return render(request,'transaction.html',{'trans':trans,'active':'btn-primary'})
 