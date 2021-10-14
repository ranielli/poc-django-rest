from django.db import models
from django.db.models.fields import CharField, EmailField
from .utils import geocode_google_maps

# Create your models here.
class Customer(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    first_name = models.CharField(max_length=50)
    last_name = CharField(max_length=100)
    email = EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    company = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    title = CharField(max_length=30)
    latitude = models.FloatField(blank=True, null= True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
    
    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        if self.city:
            longitude, latitude = geocode_google_maps(self.city)
            self.longitude = longitude
            self.latitude =  latitude
        super().save(*args, **kwargs)
