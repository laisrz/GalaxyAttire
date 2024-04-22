from django.db import models
import uuid

from localflavor.br.models import BRStateField, BRCPFField, BRPostalCodeField


def photo_path_upload_to(instance, filename):
    return "images/{}/{}".format(instance.name, filename)

class Customer(models.Model):
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    cpf = BRCPFField(unique=True)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.cpf}'
    
    class Meta:
        verbose_name = 'Cadastro de cliente'
        verbose_name_plural = 'Cadastro de clientes'
        ordering = ['-date_created']

class CustomerAddress(models.Model):
    address_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address_street = models.CharField(max_length=300)
    address_number = models.CharField(max_length=50)
    address_complemento = models.CharField(max_length=50, blank=True)
    address_cep = BRPostalCodeField()
    address_city = models.CharField(max_length=200)
    address_state = BRStateField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer} {self.address_city} {self.date_created}'
    
    class Meta:
        verbose_name = 'Cadastro de endereço de cliente'
        verbose_name_plural = 'Cadastro de endereços de clientes'
        ordering = ['-date_created']


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.name}'

class SubCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.name}'

class Collection(models.Model):
    name = models.CharField(max_length=200, unique=True)
    arrival = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=None)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, blank=True)
    description = models.TextField()
    details = models.TextField(blank=True)
    composition = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to=photo_path_upload_to)
    photo_main_alt = models.CharField(max_length=50, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Cadastro de produto'
        verbose_name_plural = 'Cadastro de produtos'
        ordering = ['-date_created']


class ProductItem(models.Model):
     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
     qtd_stock = models.PositiveIntegerField()
     price = models.DecimalField(max_digits=6, decimal_places=2)





    




    
    
    

