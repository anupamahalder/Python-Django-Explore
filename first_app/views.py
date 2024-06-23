from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def courses(request):
    return HttpResponse("This is courses page of first_app!")

def about(request):
    return HttpResponse("This is about page of first_app!")

def home(request):
    # we will send a context in the form of dictionary 
    dict = {'author': 'anupama', 'age': 20}
    return render(request, 'first_app/home.html', context=dict) # also we can directly pass dict as third parameter
    # return render(request, 'first_app/home.html', dict)
    # return render(request, 'first_app/home.html', {'author': 'anupama', 'lst':[1,2]})

def contact(request):
    return HttpResponse("This is contact page of first_app!")