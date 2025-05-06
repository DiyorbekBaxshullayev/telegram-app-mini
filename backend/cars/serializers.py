# cars/serializers.py
from rest_framework import serializers
from .models import Car, Order

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'name', 'brand', 'year', 'daily_price', 'is_active']  # Kerakli maydonlar

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'name', 'phone', 'passport', 'address', 'status', 'car']  # Buyurtma maydonlari
