from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from .models import Team

# Create your views here.
def fun(request):
    obj=Place.objects.all()
    mkv=Team.objects.all()
    return render(request,'index.html',{'result':obj,
                                                             'result2':mkv})


