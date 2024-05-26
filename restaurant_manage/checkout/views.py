from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
#view locations
def checkout(request):
    context = {}
    return render(request, 'checkout\checkout.html', context)