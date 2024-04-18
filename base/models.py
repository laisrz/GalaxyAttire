from django.db import models
from django.contrib.auth.models import User

from localflavor.br.models import BRStateField, BRCPFField, BRPostalCodeField


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
