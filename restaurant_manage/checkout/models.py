from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth import get_user_model
class Voucher(models.Model):
    code = models.CharField(max_length=12, unique=True)
    discount_type = models.CharField(
        max_length=12,
        choices=[
            ('percentage', '%'),
            ('fixed_amount', 'VND'),
        ]
    )
    discount_value = models.IntegerField()
    valid_from = models.DateTimeField(default=datetime.now())
    valid_to = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


from phonenumber_field.modelfields import PhoneNumberField
User = get_user_model()
class OrderCo(models.Model):
    user = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE, 
        related_name='orders_co', 
        null=True, 
        blank=True
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255,default="Không")
    country = models.CharField(max_length=50, default='Việt Nam')
    payment_method = models.CharField(max_length=50, default='Paypal/Credit card')
    delivery_time = models.TimeField(null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    # order_note = models.TextField(blank=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField()

    def __str__(self):
        return f'Order #{self.pk}'