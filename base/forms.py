from django import forms
from base.models import Customer
from localflavor.br.forms import BRStateSelect, BRCPFField, BRZipCodeField
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)
    password = forms.CharField(
        label='*Senha',
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control", 
                'style': 'max-width: 400px; margin: 8px -2px',
                'placeholder': 'Senha'
                }))
    class Meta:
        model = Customer
        fields = ['email', 'cpf', 'first_name', 'last_name', 'password', 'phone']
        widgets = {
            'cpf': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px; margin: 10px -2px',
                'placeholder': 'CPF',
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 400px; margin: 10px -2px',
                'placeholder': 'Email'
                }),
            'first_name': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 400px; margin: 10px -2px',
                'placeholder': 'Nome'
                }),
            'last_name': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 400px; margin: 10px -2px',
                'placeholder': 'Sobrenome'
                }),
            'phone': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 400px; margin-top: 10px; margin-left: -2px',
                'placeholder': 'Telefone'
                })
        }
        labels = {
            'email': '*Email',
            'cpf': '*CPF',
            'first_name': '*Nome',
            'last_name': '*Sobrenome',
            'phone': '*Telefone'
        }