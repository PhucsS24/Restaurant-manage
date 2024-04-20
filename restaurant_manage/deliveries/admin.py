from django.contrib import admin
from .models import Order, MenuItem
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'item', 'price']

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

admin.site.register(Order, OrderAdmin)
admin.site.register(MenuItem, MenuItemAdmin)