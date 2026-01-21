# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# Model for car make
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# <Model for car model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'wagon'),
        ('CONVERTIBLE', 'Convertible'),
        ('TRUCK', 'Truck'),
        ('COUPE', 'Coupe'),
    ]
    type = models.CharField(max_length=12, choices=CAR_TYPES, default='SEDAN')
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2026),
            MinValueValidator(2010)
        ])
    
    def __str__(self):
        return self.name

# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
