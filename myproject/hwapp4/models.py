from django.db import models

from hwapp2.models import Product


class Producthwapp4(Product):
    image = models.ImageField(upload_to='media', blank=True, null=True)
