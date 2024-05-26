from django.contrib import admin
from django.urls import path
from locations import views as locations


urlpatterns = [
    path('', locations.locations, name="locations"),

]

