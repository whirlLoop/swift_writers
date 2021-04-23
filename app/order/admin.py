from django.contrib import admin
from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['topic', 'client', 'date_created']
    list_filter = ['topic', 'client', 'date_created', 'due_date', 'status']
    search_fields = ['topic', 'client__email']
    # raw_id_fields = ['client']
