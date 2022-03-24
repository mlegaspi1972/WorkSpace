# Views for django
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hello(request):
    return HttpResponse('Hello World')

def home_view(request, *args,**kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request,"home.html",{})