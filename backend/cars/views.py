# views.py
from rest_framework import generics
from .models import Car, Order
from .serializers import CarSerializer, OrderSerializer

# Boshqa mavjud kodlar
class CarListView(generics.ListAPIView):
    queryset = Car.objects.filter(is_active=True)
    serializer_class = CarSerializer

class CarDetailView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# views.py
class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()  # Barcha buyurtmalarni olish
    serializer_class = OrderSerializer

