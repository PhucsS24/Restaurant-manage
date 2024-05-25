from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import BookTableForm
from .models import Booking
from accounts.models import CustomUser
# Create your views here.
#view home

def home(request):
    if request.method == 'POST':
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
            
            # Lưu dữ liệu vào cơ sở dữ liệu
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
            
            # Redirect hoặc render template
            return redirect('home')
    else:
        form = BookTableForm()
    
    return render(request, 'home\home.html', {'form': form})

def home(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.get(id=user_id)
        return render(request, 'home\home.html', {'user': user})
    else:
        return redirect('signin')

