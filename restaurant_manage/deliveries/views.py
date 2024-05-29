from django.shortcuts import render
from .models import MenuItem
from cart.cart import Cart
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('productId')
        quantity = int(request.POST.get('quantity'))
        item = MenuItem.objects.get(id=product_id)
        cart = Cart(request)
        cart.add(item, quantity)
    return HttpResponse("Add to cart successfully!")

def Deliveries(request):
    
    menuItems = MenuItem.objects.all()

    context = {'menuItems':  menuItems }
    return render(request, 'deliveries/deliveries_2.html', context)