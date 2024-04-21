from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_num = models.BigIntegerField()
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField()
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name


class Order(models.Model):
    products = models.ManyToManyField(Product, on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client, on_delete=models.CASCADE)
    total_sum = models.DecimalField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")
