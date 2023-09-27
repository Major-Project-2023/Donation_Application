from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html", {'navbar':'home'})

def portal(request):
    return render(request, 'paymentportal.html', {'navbar':'portal'})

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Email: {email} Password: {password}")
    return render(request, "signup.html", {'navbar':'signup'})

def login(request):
    print(request.GET)
    return render(request, 'login.html', {'navbar':'login'})