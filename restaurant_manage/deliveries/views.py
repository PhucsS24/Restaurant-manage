from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('productId')
        quantity = int(request.POST.get('quantity'))
        total = float(request.POST.get('total'))

        cart = request.session.get(settings.CARD_SESSION_ID)

        print(product_id)
        print(cart)
    return None



def Deliveries(request):
    
    menuItems = MenuItem.objects.all()

    context = {'menuItems':  menuItems }
    return render(request, 'deliveries/deliveries_2.html', context)