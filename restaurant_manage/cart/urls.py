from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_cart, name='cart'),
    path('delete_cart/', views.delete_cart, name='delete_cart'),
    path('checkout/', views.checkout, name='total')
]