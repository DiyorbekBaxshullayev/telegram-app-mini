from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cars.urls')),  # bu muhim
    path('api/cars/', CarListView.as_view(), name='car-list'),
    path('api/cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('api/orders/', OrderCreateView.as_view(), name='create-order'),
    path('api/orders/list/', OrderListView.as_view(), name='order-list'),  # Yangi endpoint qo'shildi
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    