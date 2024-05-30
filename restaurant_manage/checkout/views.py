from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from cart.cart import Cart
from datetime import datetime
import json

# Create your views here.
#view locations
def checkout(request):
    now =datetime.now()  # Sử dụng timezone.now() để lấy thời gian hiện tại
    vouchers = Voucher.objects.filter(
        is_active=True,
        valid_from__lte=now,
        valid_to__gte=now
    )
    voucher_data = [
        {
            'code': voucher.code,
            'discount_type': voucher.discount_type,
            'discount_value': float(voucher.discount_value)
        }
        for voucher in vouchers
    ]

    cart = Cart(request)
    cart_items = list(cart.__iter__())
    total_items = cart.__len__()
    total_price = cart.get_total_price()
    
    # Chuyển đổi thành JSON và đưa vào context
    context = {
        'voucher_data': json.dumps(voucher_data),
        'cart_items': cart_items,
        'total_items': total_items,
        'total_price': total_price
    }
    return render(request, 'checkout/checkout.html', context)