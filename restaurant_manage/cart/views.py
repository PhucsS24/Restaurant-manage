from django.shortcuts import render
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

# print(cart_items[1]['item'].image)
# print(cart_items[1]['item'].name)   