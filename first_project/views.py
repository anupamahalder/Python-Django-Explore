from django.http import HttpResponse
from django.shortcuts import render

def contact(request):
    return HttpResponse("This is contact page!")

def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse("This is about page!")

def index(request):
    return render(request,'index.html')