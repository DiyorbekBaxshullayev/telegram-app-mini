# cars/views.py

from django.shortcuts import render
from rest_framework import generics
from .models import Car, Order
from .serializers import CarSerializer, OrderSerializer
from .utils import send_telegram_message  # ← MUHIM
from django.http import JsonResponse

def car_list(request):
    cars = Car.objects.all().values()
    return JsonResponse(list(cars), safe=False)

class CarListView(generics.ListAPIView):
    queryset = Car.objects.filter(is_active=True)
    serializer_class = CarSerializer

class CarDetailView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        try:
            order = serializer.save()
            car_name = order.car.name
            message = (
                f"🚗 <b>Yangi buyurtma!</b>\n\n"
                f"👤 Ismi: {order.full_name}\n"
                f"📞 Telefon: {order.phone_number}\n"
                f"🚘 Mashina: {car_name}\n"
                f"📅 Sana: {order.created_at.strftime('%Y-%m-%d %H:%M')}"
            )
            send_telegram_message(message)  # ← IKINCHI BOTGA YUBORADI
        except Exception as e:
            print("❌ Xatolik yuz berdi:", e)
