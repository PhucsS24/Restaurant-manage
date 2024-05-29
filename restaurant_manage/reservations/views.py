from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import BookTableForm
from .models import Booking
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.urls import reverse


@csrf_exempt
def booking(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = BookTableForm(request.POST)
        if form.is_valid():
            # Xử lý dữ liệu
            print(form)
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
            created_at = form.cleaned_data['created_at']
            user = request.user if request.user.is_authenticated else None

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
                note=note,
                user=user,
                created_at=created_at,
            )
            booking.save()
            

            return JsonResponse({'success': True, 'message': 'Yêu cầu của bạn đã được gửi','redirect_url': reverse('reservations:booking_ok')})
        else:
            return JsonResponse({'success': False, 'message': 'Có trường bị lỗi','errors': form.errors})
    return JsonResponse({'success': False, 'message': 'Yêu cầu không hợp lệ'}, status=400)
def booking_ok(request):
    if request.user.is_authenticated:
        latest_booking = Booking.objects.filter(user=request.user).latest('created_at')
    else:
        # Lấy thông tin từ session (nếu có)
        booking_id = request.session.get('latest_booking_id')
        if booking_id:
            latest_booking = get_object_or_404(Booking, pk=booking_id)
        else:
            latest_booking = None

    context = {
        'latest_booking': latest_booking,
    }
    return render(request, 'reservations/bookok.html', context)