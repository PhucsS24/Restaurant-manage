from django import forms
from .models import Checkout

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['first_name', 'last_name', 'phone', 'email', 'address', 'note', 'delivery_date', 'delivery_time', 'payment_method']
