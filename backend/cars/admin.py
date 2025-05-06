# admin.py
from django.contrib import admin
from .models import Car, Order

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'year', 'daily_price_display', 'is_active')  # daily_price o'rniga custom method

    def daily_price_display(self, obj):
        return f"{int(obj.daily_price)} so'm"  # Narxni int shaklida chiqarish
    daily_price_display.admin_order_field = 'daily_price'  # Admin panelida tartiblash uchun

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'car', 'phone', 'status', 'created_at')  # `status`, `created_at`ni qo‘shdim
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'phone', 'passport')
