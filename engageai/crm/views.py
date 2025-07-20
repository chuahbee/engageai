from django.shortcuts import render, redirect
from .models import Customer

def customer_list(request):
    customers = Customer.objects.all().order_by('-created_at')
    return render(request, 'crm/customer_list.html', {'customers': customers})

def add_customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        source = request.POST.get('source')
        tag = request.POST.get('tag')
        Customer.objects.create(name=name, email=email, source=source, tag=tag)
        return redirect('customer_list')
    return render(request, 'crm/add_customer.html')
