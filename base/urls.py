from django.urls import path
from base.views import *

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('product/<int:id>', view_product),
    
]