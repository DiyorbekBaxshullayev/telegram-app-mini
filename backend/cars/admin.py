# cars/admin.py
from django.contrib import admin
from .models import Car, Order

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'year', 'daily_price', 'is_active')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'car', 'phone', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'phone', 'passport')
