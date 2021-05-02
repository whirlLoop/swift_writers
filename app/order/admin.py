from django.contrib import admin
from order.models import Order, OrderMaterial, TempOrderMaterial


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['topic', 'client', 'date_created']
    list_filter = ['topic', 'client', 'date_created', 'due_date', 'status']
    search_fields = ['topic', 'client__email']
    # raw_id_fields = ['client']


@admin.register(OrderMaterial)
class OrderMaterialAdmin(admin.ModelAdmin):
    list_display = ['order', 'extension', 'filename']


@admin.register(TempOrderMaterial)
class TempOrderMaterialAdmin(admin.ModelAdmin):
    list_display = ['client', 'material']
