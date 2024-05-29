from django.conf import settings
from deliveries.models import MenuItem
from decimal import Decimal
from re import sub


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def save(self):
        self.session.modified = True

    def add(self, item, quantity):
        item_id = str(item.id)
        if item_id not in self.cart:
            self.cart[item_id] = {
                'quantity': 0,
                'price': str(item.price)
            }
        self.cart[item_id]['quantity'] = quantity
        self.cart[item_id]['price']    = int(quantity * Decimal(sub(r'[^\d.]', '', str(item.price))))
        self.save()
    
    def remove(self, item):
        item_id = str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()
    
    def __iter__(self):
        item_ids = self.cart.keys()
        items = MenuItem.objects.filter(id__in=item_ids)
        cart = self.cart.copy()
        for item in items:
            cart[str(item.id)]['item'] = item
        for item in cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())
    
    def clear(self):
        for key in list(self.cart.keys()):
            del self.cart[key]
        self.save()
