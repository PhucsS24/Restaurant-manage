from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .forms import OrderFormCo
from cart.views import clear_cart
from cart.cart import Cart

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
    total_price = cart.get_total_price()
    total_price_8p=0.08*total_price
    total=total_price+total_price_8p

    context = {
        'voucher_data': json.dumps(voucher_data),
        'total_price': total_price,
        'total_price_8p': total_price_8p,
        'total': total,
    }
    return render(request, 'checkout/checkout.html', context)


@require_POST 
@csrf_exempt 
def save_orderco(request):
    data = json.loads(request.body)
    form = OrderFormCo(data)
    if form.is_valid():
        user = request.user if request.user.is_authenticated else None
        orderco = form.save(commit=False)  
        orderco.user = user
        orderco.save()
        cart = Cart(request)
        cart.clear()

        return redirect('/')  # Chuyển hướng đến trang thành công
    else:
        return render(request, 'checkout/checkout.html', {'form': form})  # Hiển thị lại form nếu có lỗi