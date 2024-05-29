from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.utils import timezone
class Booking(models.Model):
    select_location = models.CharField(max_length=100)
    select_size = models.IntegerField()
    choice_date = models.DateField()
    choice_time = models.TimeField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    size_party = models.CharField(max_length=100)
    note = models.TextField()
    created_at = models.DateTimeField()
    user = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE, 
        related_name='bookings', 
        null=True, 
        blank=True
    )