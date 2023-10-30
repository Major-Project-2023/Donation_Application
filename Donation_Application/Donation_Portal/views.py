from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from .models import Customer, Transaction,NGO
from .forms import SignupForm ,CustomerProfileForm,DonationForm,NGO_RegistrationForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
# from .models import Transaction

def home(request):
    all_ngos = NGO.objects.all()
    return render(request, 'home.html',{'ngos': all_ngos}) #{'navbar':'home'}
    
def ngo_registration(request):
    ngo_form = NGO_RegistrationForm()
    return render(request, 'NGO_registration.html', {'ngo_form':ngo_form})

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

@login_required
@csrf_exempt
def portal(request):
    user = request.user
    ngo_id = request.GET.get('ngo_id')
    ngo = get_object_or_404(NGO, id=ngo_id)
    country = request.GET.get('country')
    form = DonationForm(request.POST or None)  # Initialize form

    if request.method == 'POST':
        if form.is_valid():
            amount = form.cleaned_data['amount']
            # Create PayPal dictionary
            paypal_dict = {
                "cmd" : "_donations",
                "business": settings.PAYPAL_RECEIVER_EMAIL[country],
                "amount": amount,
                "item_name": ngo.name,
                "invoice": f"invoice-{ngo_id}",
                "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
                "return": request.build_absolute_uri(reverse('successful')),
                "cancel_return": request.build_absolute_uri(reverse('cancelled')),
                "custom": user,
            }
            # Create PayPal form
            paypal_form = PayPalPaymentsForm(initial=paypal_dict, button_type="donate")
            return render(request, "paymentportal.html", {'form': form, 'paypal_form': paypal_form})

    return render(request, 'paymentportal.html', {'form': form})

@csrf_exempt
def successful(request):
    return render(request,'successful.html')

def cancelled(request):
    return render(request,'cancelled.html')


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


@method_decorator(login_required,name='dispatch')
class TransactionView(View):
    def get(self,request):
        trans = Transaction.objects.filter(sender=request.user)
        return render(request,'transaction.html',{'trans':trans,'active':'btn-primary'})
 

def NGO_Registration(request):
    if request.POST:
        form = NGO_RegistrationForm(request.POST,request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect(home)
    return render(request,'NGO_registration.html',{'form':NGO_RegistrationForm})