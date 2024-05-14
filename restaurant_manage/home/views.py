from django.shortcuts import render, redirect
from accounts.models import CustomUser
# Create your views here.
#view home

def home(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.get(id=user_id)
        return render(request, 'home\home.html', {'user': user})
    else:
        return redirect('signin')

#view event
def event(request):
    context = {}
    return render(request, 'event\event.html', context)

#view menu
def menu(request):
    context = {}
    return render(request, 'menu\menu.html', context)

def signup(request):
    context = {}
    return render(request, 'signin_signup\signup.html', context)

def signin(request):
    context = {}
    return render(request, 'signin_signup\signin.html', context)
