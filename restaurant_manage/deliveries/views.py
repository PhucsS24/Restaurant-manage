from django.shortcuts import render
from .models import MenuItem, Order

# Create your views here.

def delivery(request):
    items = MenuItem.objects.all()
    return render(request, 'deliveries/base.html', {'items': items })