from django.shortcuts import render
from deliveries.models import Order
# Create your views here.
def cart(request):
    # user_id = request.session.get('user_id')
    # if user_id:
        #order = Order.objects.get(user=user_id)
        #print(order)
        return render(request, 'cart/cart.html')