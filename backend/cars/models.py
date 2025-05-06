# cars/models.py
from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    year = models.IntegerField()
    daily_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.name} ({self.year})"

class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    passport = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('new', 'New'), ('approved', 'Approved')], default='new')
    car = models.ForeignKey(Car, related_name='orders', on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id} - {self.name}"
