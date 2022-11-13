from django.contrib import admin
from .models import ProductInfo, OrderInfo

# Register your models here.
@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    list_display = [x for x in list(ProductInfo._meta._forward_fields_map.keys())]

@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    list_display = [x for x in list(OrderInfo._meta._forward_fields_map.keys())]