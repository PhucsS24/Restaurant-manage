from django.contrib import admin
from .models import Order, MenuItem
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'item', 'formatted_price', 'quantity', 'created_at', 'updated_at']

    def formatted_price(self, obj):
        return f"{obj.price.amount} {obj.price.currency}"
    formatted_price.short_description = 'price'

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'formatted_price']

    def formatted_price(self, obj):
        return f"{obj.price.amount} {obj.price.currency}"
    formatted_price.short_description = 'price'

admin.site.register(Order, OrderAdmin)
admin.site.register(MenuItem, MenuItemAdmin)