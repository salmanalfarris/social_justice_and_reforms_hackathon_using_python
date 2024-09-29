from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class User(AbstractUser):
    # Add custom fields here
    USER_ROLES = (
        ('citizen', 'Citizen'),
        ('lawyer', 'Lawyer'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=USER_ROLES, default='citizen')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
    

class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.product_name} - {self.quantity}'  