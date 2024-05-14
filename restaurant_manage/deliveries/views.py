from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def Deliveries(request):
    
    menuItems = MenuItem.objects.all()

    context = {'menuItems':  menuItems }
    return render(request, 'deliveries/deliveries.html', context)