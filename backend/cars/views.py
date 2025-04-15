from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Car, Order
from .serializers import CarSerializer, OrderSerializer

class CarListView(generics.ListAPIView):
    queryset = Car.objects.filter(is_active=True)
    serializer_class = CarSerializer

class CarDetailView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
