from django.shortcuts import render
from base.forms import RegisterForm
from base.models import Customer, Product

def index(request):
    arrivals = Product.objects.filter(arrival=True)
    return render(request, 'index.html', {'arrivals': arrivals})

def register(request):
    success = False 
    form = RegisterForm()

    if request.method == "POST":
    
        form = RegisterForm(request.POST or None)
        
        if form.is_valid():
            success = True
            customer = form.save()

            return render(request, 'index.html', {'customer': Customer.objects.get(email=customer.email)})
    
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'register.html', context)
