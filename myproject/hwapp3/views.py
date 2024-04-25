from datetime import timedelta, datetime
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from hwapp2.models import Order, Product, Client


def client_orders(request, client_pk):
    client = get_object_or_404(Client, pk=client_pk)
    orders = Order.objects.filter(customer=client).order_by('created_at')

    return render(request, 'hwapp3/client_orders.html', {'orders': orders})


def client_orders_by_date(request, client_pk, days):
    client = get_object_or_404(Client, pk=client_pk)
    orders = Order.objects.filter(customer=client).filter(created_at__range=[
        str(datetime.now() - timedelta(days)), str(datetime.now())]).order_by('created_at')
    

    return render(request, 'hwapp3/client_orders.html', {'orders': orders})


def index(request):
    clients = Client.objects.all()

    return render(request, 'hwapp3/clients.html', {'clients': clients})
