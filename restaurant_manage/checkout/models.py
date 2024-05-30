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

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='checkouts', null=True, blank=True)
    first_name = models.CharField("Họ", max_length=100)
    last_name = models.CharField("Tên", max_length=100)
    phone = PhoneNumberField("Số điện thoại")
    email = models.EmailField("Email")
    address = models.TextField("Địa chỉ", null=True, blank=True)  
    note = models.TextField("Ghi chú", null=True, blank=True)
    delivery_date = models.DateField("Ngày giao hàng", null=True, blank=True)
    delivery_time = models.TimeField("Thời gian giao hàng", null=True, blank=True)
    subtotal = models.DecimalField("Tổng tiền", max_digits=10, decimal_places=2, default=0)
    shipping_fee = models.DecimalField("Phí ship", max_digits=10, decimal_places=2, default=0)
    vat = models.DecimalField("Thuế", max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField("Tổng cộng", max_digits=10, decimal_places=2, default=0)

    PAYMENT_METHOD_CHOICES = [
        ('paypal', 'PayPal/Credit Card'),
        ('cod', 'Cash on Delivery'),
    ]
    payment_method = models.CharField("Phương thức thanh toán", max_length=11, choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return f"Đơn hàng #{self.pk} của {self.user}"