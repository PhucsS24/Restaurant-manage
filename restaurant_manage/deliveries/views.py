from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def add_to_cart(request):

    return None



def Deliveries(request):
    
    menuItems = MenuItem.objects.all()

    context = {'menuItems':  menuItems }
    return render(request, 'deliveries/deliveries_2.html', context)