from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField(validators=[MinValueValidator(1)])
    booking_date = models.DateTimeField()
    
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    