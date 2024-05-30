from django.urls import path
from . import views


urlpatterns = [
    path('', views.deliveries, name='delivery'),
    path('add-to-cart/', views.add_to_cart, name='addToCart')
]
