# from django.http import  HttpResponse
from django.shortcuts import render,redirect

def homepage(request):
    # return HttpResponse("Hello World! I'm Home. ")
    return  render(request,'home.html')

def about(request):
    # return HttpResponse('My About Page.')
    return render (request,"about.html")

# def register(request):
#     # return HttpResponse('My Register Page.')
#     return render (request,"register.html")