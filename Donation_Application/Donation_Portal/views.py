from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "./template/home.html", context=home)
    # return HttpResponse("<H1>Home</H1>")
