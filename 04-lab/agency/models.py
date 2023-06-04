from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser, Group, Permission

class Climate(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)
    climates = models.ManyToManyField(Climate, related_name='countries')

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='hotels')
    star_rating = models.IntegerField(default=0)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField(default="no address")
    phone = models.CharField(max_length=20, default='')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Employee(AbstractUser):
    groups = models.ManyToManyField(Group, blank=True, related_name='employee_groups')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='employee_user_permissions')



class Package(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    hotels = models.ManyToManyField(Hotel)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    duration = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, related_name='created_packages')

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
    order_date = models.DateField(default=datetime.now)

    def __str__(self):
        return f'Order for {self.client}'
