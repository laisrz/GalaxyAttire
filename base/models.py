from django.db import models
import uuid

from localflavor.br.models import BRStateField, BRCPFField, BRPostalCodeField
from multiselectfield import MultiSelectField


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    cpf = BRCPFField(unique=True)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address_street = models.CharField(max_length=300)
    address_number = models.CharField(max_length=50)
    address_complemento = models.CharField(max_length=50, blank=True)
    address_cep = BRPostalCodeField()
    address_city = models.CharField(max_length=200)
    address_state = BRStateField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.cpf} {self.email}'
    
    class Meta:
        verbose_name = 'Cadastro de cliente'
        verbose_name_plural = 'Cadastro de clientes'
        ordering = ['-date_created']

def photo_path_upload_to(instance, filename):
    return "images/{}/{}/{}".format(instance.product.category, instance.product.code, filename)

class Product(models.Model):
    categories = (
        ('FE', 'Feminino'),
        ('MA', 'Masculino'),
        ('IN', 'Infantil'),
        ('BE', 'Beleza'),
        ('BA', 'Básicos'),
        ('JE', 'Jeans'),
        ('AC', 'Acessórios'),
        ('ES', 'Esportivos'),
        ('MO', 'Moda Íntima')
    )

    sub_categories = (
        ('Calça', 'Calça'),
        ('Blusa', 'Blusa'),
        ('Blazer', 'Blazer'),
        ('Shorts', 'Shorts'),
        ('Camisa', 'Camisa'),
        ('Camiseta', 'Camiseta'),
        ('Moletom', 'Moletom'),
        ('Saia', 'Saia'),
        ('Vestido', 'Vestido'),
        ('Top', 'Top'),
        ('Legging', 'Legging'),
        ('Calcinha', 'Calcinha'),
        ('Cueca', 'Cueca'),
        ('Pijama', 'Pijama'),
        ('Meia', 'Meia'),
        ('Sutiã', 'Sutiã'),
        ('Bermuda', 'Bermuda'),
        ('Terno', 'Terno'),
        ('Anéis', 'Anéis'),
        ('Bolsas', 'Bolsas'),
        ('Bonés', 'Bonés'),
        ('Brincos', 'Brincos'),
        ('Cachecol', 'Cachecol'),
        ('Carteiras', 'Carteiras'),
        ('Cintos', 'Cintos'),
        ('Colares', 'Colares'),
        ('Óculos', 'Óculos'),
        ('Relógios', 'Relógios'),
        ('Lábios', 'Lábios'),
        ('Olhos', 'Olhos'),
        ('Rosto', 'Rosto'),
        ('Unhas', 'Unhas'),
        ('Perfume', 'Perfume'),
        ('Banho', 'Banho'),
        ('Pós-Banho', 'Pós-Banho')      
    )

    colors = (
        ('Branco', 'Branco'),
        ('Preto', 'Preto'),
        ('Azul', 'Azul'),
        ('Rosa', 'Rosa'),
        ('Vermelho', 'Vermelho'),
        ('VE', 'Verde Escuro'),
        ('AE', 'Azul Escuro'),
        ('Cinza', 'Cinza'),
        ('Laranja', 'Laranja'),
        ('Bege', 'Bege')
    )
  
    code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    collection = models.CharField(max_length=200, blank=True)
    arrival = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock_size_P = models.PositiveIntegerField()
    stock_size_M = models.PositiveIntegerField()
    stock_size_G = models.PositiveIntegerField()
    stock_size_GG = models.PositiveIntegerField()
    category = models.CharField(max_length=10, choices=categories)
    sub_category = models.CharField(max_length=50, choices=sub_categories)
    color = MultiSelectField(max_length=10, choices=colors)
    description = models.TextField()
    details = models.TextField(blank=True)
    composition = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to=photo_path_upload_to)
    photo_main_alt = models.CharField(max_length=50, blank=True)
    photo_2 = models.ImageField(upload_to=photo_path_upload_to, blank=True)
    photo_2_alt = models.CharField(max_length=50, blank=True)
    photo_3 = models.ImageField(upload_to=photo_path_upload_to, blank=True)
    photo_3_alt = models.CharField(max_length=50, blank=True)
    photo_4 = models.ImageField(upload_to=photo_path_upload_to, blank=True)
    photo_4_alt = models.CharField(max_length=50, blank=True)
    photo_5 = models.ImageField(upload_to=photo_path_upload_to, blank=True)
    photo_5_alt = models.CharField(max_length=50, blank=True)
    photo_6 = models.ImageField(upload_to=photo_path_upload_to, blank=True)
    photo_6_alt = models.CharField(max_length=50, blank=True)
    sale = models.BooleanField(default=False)
    percentage_discount = models.PositiveIntegerField(blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.category} {self.sub_category} {self.price}'
    
    class Meta:
        verbose_name = 'Cadastro de produto'
        verbose_name_plural = 'Cadastro de produtos'
        ordering = ['-date_created']
    