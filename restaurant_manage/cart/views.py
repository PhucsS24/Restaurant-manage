from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from deliveries.models import MenuItem
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

@require_POST
def delete_cart(request):
    item_id = request.POST.get('itemId')
    if item_id:
        try:
            item = MenuItem.objects.get(id=item_id)
            cart = Cart(request)
            cart.remove(item)
            cart_items = cart.serialize_cart_items()
            return JsonResponse({'success': True, 'cart_items': cart_items})
        except MenuItem.DoesNotExist:
            return JsonResponse({'success': True, 'error':'Item not found'})
    return JsonResponse({'success': True, 'error':'Invalid request'})