from django.db import models
from restaurant.models import *
# Create your models here.



class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.full_name





class OrderToDelivery(models.Model):
    customer = models.CharField(max_length=100)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True)
    status = models.BooleanField()


class Address(models.Model):
    endpoint = models.CharField(max_length=60)
    order = models.ForeignKey(OrderToDelivery, on_delete=models.SET_NULL, null=True, related_name='endpoint')

    def __str__(self):
        return self.endpoint


