from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("HOME")

def about(request):
    return render(request,'abc.html')

def contact(request):
    return HttpResponse("CONTACT")

def details(request):
    return render(request,'bcc.html')

def thanks(request):
    return HttpResponse("THANKS")