from django.db import models




models.py
class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    daily_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='car_images/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

models.py

# class Car(models.Model):
#     title = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='cars/')
#     # boshqa field'lar...

#     def __str__(self):
#         return self.title



class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Yangi'),
        ('approved', 'Tasdiqlangan'),
        ('rejected', 'Rad etilgan'),
        ('completed', 'Yakunlangan'),
    ]
    
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    passport = models.CharField(max_length=50)
    address = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.car.name} ({self.status})"

