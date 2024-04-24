from django.contrib import admin

from .models import Client, Product, Order


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Client)
