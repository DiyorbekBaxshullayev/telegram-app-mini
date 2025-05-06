# cars/views.py
from rest_framework import generics
from .models import Car, Order
from .serializers import CarSerializer, OrderSerializer
from django.http import JsonResponse

# Barcha buyurtmalarni olish uchun ListAPIView
class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()  # Buyurtmalarni olish
    serializer_class = OrderSerializer  # Serializer ni ko'rsatyapmiz

# Avtomobillar ro'yxatini olish
class CarListView(generics.ListAPIView):
    queryset = Car.objects.filter(is_active=True)
    serializer_class = CarSerializer

# Avtomobil haqida batafsil ma'lumot olish
class CarDetailView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

# Buyurtma yaratish
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
