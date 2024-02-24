from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):  
    name = models.CharField(null=False, max_length=30, default='punch')
    description = models.CharField(null=False, max_length=30, default='900 cc, front wheel drive')
    def __str__(self):
        return self.name

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarModel(models.Model):
    carMakers = models.ForeignKey(CarMake,on_delete= models.CASCADE)
    name = models.CharField(null=False, max_length=30, default='nexa')
    dealerID = models.CharField(null=False, max_length=30, default='32156s3df16asd1f35asdf')
    type = models.CharField(null=False, max_length=30, default='front wheel drive',choices=[('Sedan','Sedan'), ('SUV','SUV'),  ('WAGON','WAGON')])
    year = models.DateField(null=False)

    def __str__(self):
        return self.name + " " + self.dealerID


class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name
# <HINT> Create a plain Python class `DealerReview` to hold review data
