from django.contrib import admin
from base.models import *

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'cpf', 'email']
    search_fields = ['first_name', 'last_name', 'cpf', 'email']
    list_filter = ['date_created']

@admin.register(CustomerAddress)
class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'address_city', 'date_created']
    search_fields = ['customer', 'address_city']
    list_filter = ['date_created']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'collection']
    search_fields = ['name', 'collection']
    list_filter = ['date_created']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'price']
