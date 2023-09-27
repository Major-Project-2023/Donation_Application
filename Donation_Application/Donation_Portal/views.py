from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html", {'navbar':'home'})

def portal(request):
    return render(request, 'paymentportal.html', {'navbar':'portal'})

def signup(request):
    if request.method == 'POST':
        print(request.POST.get('email'),"\n",request.POST.get('password'))
    return render(request, "signup.html", {'navbar':'signup'})

def login(request):
    print(request.GET)
    return render(request, 'login.html', {'navbar':'login'})