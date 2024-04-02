from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#view home
def home(request):
    context = {}
    return render(request, 'app\home\home.html', context)

#view event
def event(request):
    context = {}
    return render(request, 'app\event\event.html', context)


def signup(request):
    context = {}
    return render(request, 'app\signin_signup\signup.html', context)

def signin(request):
    context = {}
    return render(request, 'app\signin_signup\signin.html', context)
