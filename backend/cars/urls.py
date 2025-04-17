# from django.urls import path
# from .views import CarListView, CarDetailView, OrderCreateView

# urlpatterns = [
#     path('cars/', CarListView.as_view(), name='car-list'),
#     path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
#     path('orders/', OrderCreateView.as_view(), name='create-order'),
# ]

from django.urls import path
from .views import CarListView, CarDetailView, OrderCreateView

urlpatterns = [
    path('api/cars/', CarListView.as_view(), name='car-list'),
    path('api/cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('api/orders/', OrderCreateView.as_view(), name='create-order'),
]
