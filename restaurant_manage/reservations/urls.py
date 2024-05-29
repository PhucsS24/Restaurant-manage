from django.urls import path
from . import views
app_name = 'reservations'
urlpatterns = [path('booking/', views.booking, name="booking"),
path('booking_ok/', views.booking_ok, name="booking_ok")
]
