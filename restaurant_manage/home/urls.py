from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('events/', views.events, name="events"),
    path('logout/', views.custom_logout, name='logout'),
]

