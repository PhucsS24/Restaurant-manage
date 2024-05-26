from django.contrib import admin
from django.urls import path
from checkout import views as checkout


urlpatterns = [
    path('', checkout.checkout, name="checkout"),

]

