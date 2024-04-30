import datetime
from random import randint
import random

from django.core.management.base import BaseCommand

from hwapp.models import Client, Order, Product


class Command(BaseCommand):
    help = "Generate fake client, product and orders"

    def add_arguments(self, parser) -> None:
        parser.add_argument('clients', type=int, help='User ID')
        parser.add_argument('products', type=int, help='Product ID')
        parser.add_argument('orders', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        clients_count = kwargs.get('clients')
        products_count = kwargs.get('products')
        orders_count = kwargs.get('orders')

        start_date = datetime.datetime.now() - datetime.timedelta(days=600)
        end_date = datetime.datetime.now()

        for i in range(1, clients_count):
            client = Client(name=f'Client-{i}')
            client.save()

        for j in range(1, products_count):
            product = Product(name=f'Product-{j}')
            product.save()

        for k in range(1, orders_count):
            cus = Client.objects.get(pk=randint(1, clients_count))
            prod = Product.objects.get(pk=randint(1, products_count))
            order = Order(customer=cus)
            order.save()
            order.products.add(prod)
            order.created_at = start_date + \
                (end_date - start_date) * random.random()
            order.save()
