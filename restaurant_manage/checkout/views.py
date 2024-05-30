from django.shortcuts import render
from django.http import HttpResponse
from .models import *
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

    # Chuyển đổi thành JSON và đưa vào context
    context = {
        'voucher_data': json.dumps(voucher_data)
    }
    return render(request, 'checkout/checkout.html', context)