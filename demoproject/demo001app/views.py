from django.shortcuts import render

# Create your views here.
def input(request):
    return render(request,'input.html')

def output(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    adn=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return render(request,'result.html',{'res1':adn,
                                                              'res2':sub,
                                                              'res3':mul,
                                                              'res4':div})