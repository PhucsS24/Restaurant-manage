from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
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