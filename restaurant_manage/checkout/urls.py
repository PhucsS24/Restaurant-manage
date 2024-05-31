from django.contrib import admin
from django.urls import path
from checkout import views as checkout
from . import views


urlpatterns = [
    path('', checkout.checkout, name="checkout"),
    path('save/', views.save_orderco, name="save_order"),

]

