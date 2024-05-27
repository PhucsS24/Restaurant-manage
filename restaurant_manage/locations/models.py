from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Restaurant(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    time_open = models.CharField(max_length=50)
    phone = PhoneNumberField(blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='location_items/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    