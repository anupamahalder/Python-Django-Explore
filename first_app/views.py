from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def courses(request):
    return HttpResponse("This is courses page of first_app!")

def about(request):
    return HttpResponse("This is about page of first_app!")

def home(request):
    # we will send a context in the form of dictionary 
    courses = [
        {'id': 1, 'name': 'python', 'fee': 5000.00},
        {'id': 2, 'name': 'C++', 'fee': 3000.00},
        {'id': 3, 'name': 'Django', 'fee': 4500.00},
        {'id': 4, 'name': 'C', 'fee': 2000.00},
    ]
    dict = {'author': 'anupama', 'age': 15, 'nums':[1,2,3,4], 'lst': ['Python', 'is', 'the', 'best'], 'courses':courses, 'birthday': datetime.datetime.now(), 'val':''}
    return render(request, 'first_app/home.html', context=dict) # also we can directly pass dict as third parameter
    # return render(request, 'first_app/home.html', dict)
    # return render(request, 'first_app/home.html', {'author': 'anupama', 'lst':[1,2]})

def contact(request):
    return HttpResponse("This is contact page of first_app!")