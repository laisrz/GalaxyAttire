from django.contrib import admin
from base.models import Customer, Product

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'cpf', 'email']
    search_fields = ['first_name', 'last_name', 'cpf', 'email']
    list_filter = ['date_created']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    search_fields = ['name', 'category', 'price', 'collection']
    list_filter = ['date_created']
