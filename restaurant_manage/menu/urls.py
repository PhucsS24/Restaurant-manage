from django.contrib import admin
from django.urls import path
from menu import views as menu


urlpatterns = [
    path('', menu.menu, name="menu"),

]

