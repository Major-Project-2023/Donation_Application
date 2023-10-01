from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from .models import Customer
from .forms import SignupForm ,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def home(request):
    return render(request, "home.html", {'navbar':'home'})

def portal(request):
    return render(request, 'paymentportal.html', {'navbar':'portal'})

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
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'profile.html',{'form':form,'active':'btn-primary'})
 
    def post(self,request):
        form = CustomerProfileForm(request.POST) 
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
            return render(request,'profile.html',{'form':form,'active':'btn-primary'})
        else:
            messages.MessageFailure(request,'Oh! No! ProfileUpdate Was Un-Successful')
            return render(request,'profile.html',{'form':form,'active':'btn-primary'})