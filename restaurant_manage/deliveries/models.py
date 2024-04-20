from django.db import models
from django.conf import settings
from djmoney.models.fields import MoneyField

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders',
        related_query_name='order'
        )
    item = models.ForeignKey('MenuItem', on_delete=models.CASCADE)
    price = MoneyField(
        max_digits=14,
        decimal_places=0,
        default_currency='VND'
        )
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = MoneyField(
        max_digits=14,
        decimal_places=0,
        default_currency='VND'
        )
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='menu_items/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

