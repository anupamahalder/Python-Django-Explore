from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def courses(request):
    return HttpResponse("This is courses page of first_app!")

def about(request):
    return HttpResponse("This is about page of first_app!")

def home(request):
    return render(request, 'first_app/home.html')

def contact(request):
    return HttpResponse("This is contact page of first_app!")