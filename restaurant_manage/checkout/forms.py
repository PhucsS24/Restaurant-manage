from django import forms
from .models import OrderCo
import datetime

class OrderFormCo(forms.ModelForm):
    class Meta:
        model = OrderCo
        # fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'delivery_date', 'delivery_time', 'order_note','order_total','created_at']
        fields = ['first_name', 'last_name', 'email', 'phone','created_at','address','country','payment_method','order_total', 'delivery_date', 'delivery_time']
        # fields = ['first_name', 'last_name', 'email', 'phone','created_at','address','country','payment_method','order_total']
    def clean_created_at(self):
        created_at = self.cleaned_data.get('created_at')
        created_at = datetime.datetime.now()  # Lấy thời gian hiện tại
        return created_at



