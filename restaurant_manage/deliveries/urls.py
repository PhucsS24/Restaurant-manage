from django.urls import path
from . import views


urlpatterns = [
    path('', views.Deliveries, name='delivery'),
    path('add-to-cart/', views.add_to_cart, name='addToCart')
]
