from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import BookTableForm
from .models import Booking
from accounts.models import CustomUser
# Create your views here.

def home(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.get(id=user_id)
        return render(request, 'home\home.html', {'user': user})
    else:
        return redirect('signin')

