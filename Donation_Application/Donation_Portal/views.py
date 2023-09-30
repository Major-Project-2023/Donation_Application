from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from .models import Customer
from .forms import SignupForm
# CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def home(request):
    return render(request, "home.html", {'navbar':'home'})

def portal(request):
    return render(request, 'paymentportal.html', {'navbar':'portal'})

# def signup(request):
#     return render(request, "signup.html", {'navbar':'signup'})
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
 
# def login(request):
#     return render(request, 'login.html', {'navbar':'login'})