from datetime import timedelta, datetime
from django.shortcuts import redirect, render, get_object_or_404

from .models import Order, Client
from .forms import ProductForm


def index(request):
    clients = Client.objects.all()

    return render(request, 'hwapp/clients.html', {'clients': clients})


def about(request):
    return render(request, 'hwapp/about.html')


def client_orders(request, client_pk):
    client = get_object_or_404(Client, pk=client_pk)
    orders = Order.objects.filter(customer=client).order_by('created_at')

    return render(request, 'hwapp/client_orders.html', {'orders': orders})


def client_orders_by_date(request, client_pk, days):
    client = get_object_or_404(Client, pk=client_pk)
    orders = Order.objects.filter(customer=client).filter(created_at__range=[
        str(datetime.now() - timedelta(days)), str(datetime.now())]).order_by('created_at')

    return render(request, 'hwapp/client_orders.html', {'orders': orders})


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        return redirect('hwapp:index')

    else:
        form = ProductForm()

    return render(request, 'hwapp/product_form.html', {'form': form})
