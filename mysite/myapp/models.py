from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.price}"

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, related_name='orders', on_delete=models.CASCADE)
    products = models.ForeignKey(Product, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order {self.id} by {self.client.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_at_the_time = models.DecimalField(max_digits=10, decimal_places=2)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_amount = models.IntegerField(default=1)
