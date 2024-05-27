from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
#view locations
def menu(request):
    menuItems = MenuItem.objects.all()
    context = {'menuItems':  menuItems }

    return render(request, 'menu\menu.html', context)