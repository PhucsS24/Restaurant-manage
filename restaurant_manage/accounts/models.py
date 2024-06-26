from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class CustomUser(AbstractUser):
    phone = PhoneNumberField(blank=True)
    
    def __str__(self):
        return self.username
    
