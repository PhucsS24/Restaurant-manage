from django.contrib import admin
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    model = Restaurant
    list_display = ["address"]

# Register your models here.
admin.site.register(Restaurant, RestaurantAdmin)