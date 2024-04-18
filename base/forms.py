from django import forms
from base.models import Customer
from localflavor.br.forms import BRStateSelect, BRCPFField, BRZipCodeField

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Customer
        fields = ['email', 'cpf', 'first_name', 'last_name', 'password', 'phone']