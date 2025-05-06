# urls.py
from django.urls import path
from .views import CarListView, CarDetailView, OrderCreateView, OrderListView

urlpatterns = [
    path('api/cars/', CarListView.as_view(), name='car-list'),
    path('api/cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('api/orders/', OrderCreateView.as_view(), name='create-order'),
    path('api/orders/list/', OrderListView.as_view(), name='order-list'),  # Yangi endpoint
]
