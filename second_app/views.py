from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def courses(request):
    return HttpResponse("This is courses page of second_app!")

def about(request):
    return HttpResponse("This is about page of second_app!")

def home(request):
    return HttpResponse("This is home page of second_app!")