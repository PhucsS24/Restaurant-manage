from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('event/', views.event, name="event"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
]
