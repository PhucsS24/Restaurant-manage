from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
#view locations
def locations(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants }
    return render(request, 'locations\locations.html', context)