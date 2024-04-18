from django.contrib import admin
from base.models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'cpf', 'email']
    search_fields = ['first_name', 'last_name', 'cpf', 'email']
    list_filter = ['date_created']


