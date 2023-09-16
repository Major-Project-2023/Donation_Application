from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html", {'navbar':'home'})

def portal(request):
    return render(request, 'paymentportal.html', {'navbar':'portal'})

def signup(request):
    return render(request, "signup.html", {'navbar':'signup'})

def login(request):
    return render(request, 'login.html', {'navbar':'login'})