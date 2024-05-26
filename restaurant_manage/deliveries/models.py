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

    # ITEM_TYPE_CHOICES = {
    #     'BEEF': 'Beef',
    #     'SAUCES': 'Sauces',
    #     'DESSERT': 'Dessert',
    #     'DRINK': 'Drink',
    #     'SOUP': 'Soup',
    #     'TRADITIONAL': 'Traditional',
    #     'POPULAR' : 'Popular'
    # }
    # item_type = models.CharField(max_length=20, choices=ITEM_TYPE_CHOICES, default='POPULAR')

    # WEIGHT_CHOICES = {
    #     250 : '250g',
    #     350 : '350g',
    #     200 : '200G',
    #     300 : '300g',
    #     500 : '500g'
    # }
    # weight = models.IntegerField(choices=WEIGHT_CHOICES, blank=True, null=True)

    # DONENESS_CHOICES = {
    #     'WELL_DONE': 'WELL DONE',
    #     'MEDIUM': 'MEDIUM',
    #     'RARE': 'RARE'
    # }
    ITEM_TYPE_CHOICES = [
        ('BEEF', 'Beef'),
        ('SAUCES', 'Sauces'),
        ('DESSERT', 'Dessert'),
        ('DRINK', 'Drink'),
        ('SOUP', 'Soup'),
        ('TRADITIONAL', 'Traditional'),
        ('POPULAR' , 'Popular')
    ]
    WEIGHT_CHOICES = [
        (250, '250g'),
        (350, '350g'),
        (200, '200g'),
        (300, '300g'),
        (500, '500g'),
    ]
    weight = models.IntegerField(choices=WEIGHT_CHOICES, blank=True, null=True)

    DONENESS_CHOICES = [
        ('WELL_DONE', 'WELL DONE'),
        ('MEDIUM', 'MEDIUM'),
        ('RARE', 'RARE'),
    ]

    doneness = models.CharField(max_length=20, choices=DONENESS_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    
    

