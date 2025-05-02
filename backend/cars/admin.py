# from django.contrib import admin
# from .models import Car, Order

# @admin.register(Car)
# class CarAdmin(admin.ModelAdmin):
#     list_display = ('name', 'brand', 'year', 'daily_price', 'is_active')

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('name', 'car', 'phone', 'status', 'created_at')
#     list_filter = ('status', 'created_at')
#     search_fields = ('name', 'phone', 'passport')





from django.contrib import admin
from .models import Car, Order

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'year', 'daily_price_display', 'is_active')  # daily_price o'rniga custom method

    # Narxni formatlash uchun maxsus method
    def daily_price_display(self, obj):
        return f"{int(obj.daily_price):,} so'm"  # Narxni to'liq son sifatida va "so'm" qo'shib ko'rsatish
    daily_price_display.admin_order_field = 'daily_price'  # Admin panelida tartiblash uchun

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'car', 'phone', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'phone', 'passport')
