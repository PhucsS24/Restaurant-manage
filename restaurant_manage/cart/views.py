from django.shortcuts import render
from django.http import HttpResponse
from .cart import Cart

# Create your views here.
def show_cart(request):
    cart = Cart(request)
    cart_items = list(cart.__iter__())
    total_items = cart.__len__()
    total_price = cart.get_total_price()

    context = {
        'cart_items': cart_items,
        'total_items': total_items,
        'total_price': total_price
    }
    return render(request, 'cart/cart.html', context)

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return HttpResponse("Clear all cart")

def delete_cart(request):
    cart = Cart(request)
    #cart.remove
    return HttpResponse("Delete a cart")