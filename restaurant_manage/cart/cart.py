from django.conf import settings
from deliveries.models import MenuItem

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def save(self):
        self.session.modified = True

    def add(self, item, quantity=1, override_quantity=False):
        item_id = str(item.id)
        if item_id not in self.cart:
            self.cart[item_id] = {
                'quantity': 0,
                'price': str(item.price)
            }
        if override_quantity:
            self.cart[item_id]['quantity'] = quantity
        else:
            self.cart[item_id]['quantity'] += quantity
        self.save()
    
    def remove(self, item):
        item_id = str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()
    
    # def __iter__(self):
    #     item_ids = self.cart.keys()
    #     items = MenuItem.objects.filter(id__in=item_ids)