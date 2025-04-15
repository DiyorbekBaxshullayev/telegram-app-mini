# from django.urls import path
# from .views import CarListView, CarDetailView, OrderCreateView

# urlpatterns = [
#     path('cars/', CarListView.as_view(), name='car-list'),
#     path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
#     path('orders/', OrderCreateView.as_view(), name='create-order'),
# ]

from django.urls import path
from .views import car_list

urlpatterns = [
    path('api/cars/', car_list, name='car_list'),
]
