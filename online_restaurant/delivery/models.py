from django.db import models



# Create your models here.
from restaurant.models import Order


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


