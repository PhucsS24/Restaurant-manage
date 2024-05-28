from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import BookTableForm
from .models import Booking
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


@csrf_exempt
def booking(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = BookTableForm(request.POST)
        if form.is_valid():
            # Xử lý dữ liệu
            select_location = form.cleaned_data['select_location']
            select_size = form.cleaned_data['select_size']
            choice_date = form.cleaned_data['choice_date']
            choice_time = form.cleaned_data['choice_time']
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            size_party = form.cleaned_data['size_party']
            note = form.cleaned_data['note']

            # Lưu dữ liệu 
            booking = Booking(
                select_location=select_location,
                select_size=select_size,
                choice_date=choice_date,
                choice_time=choice_time,
                fname=fname,
                lname=lname,
                phone=phone,
                email=email,
                size_party=size_party,
                note=note
            )
            booking.save()

            return JsonResponse({'success': True, 'message': 'Yêu cầu của bạn đã được gửi'})
        else:
            return JsonResponse({'success': False, 'message': 'Có trường bị lỗi','errors': form.errors})
    return JsonResponse({'success': False, 'message': 'Yêu cầu không hợp lệ'}, status=400)
