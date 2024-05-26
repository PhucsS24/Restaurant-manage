from django.urls import path
from . import views
app_name = 'reservations'
urlpatterns = [path('booking/', views.booking, name="booking")
]
