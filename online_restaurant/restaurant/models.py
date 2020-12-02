from django.db import models


# Create your models here.

class Menu(models.Model):
    category = (
        ('pizza','pizza'),
        ('soups','soups'),
        ('bbq','bbq'),
        ('burgers','burgers'),
        ('noodles','noodles'),
        ('drinks','drinks'),
    )
    name = models.CharField(max_length=100)
    menu_types = models.CharField(max_length=100, choices=category)
    description = models.CharField(max_length=100)
    weight = models.IntegerField(default=0)
    price = models.IntegerField()


    def __str__(self):
        return self.name


class Table(models.Model):
    table_number = models.IntegerField(default=0)

class Waiter(models.Model):
    waiter = models.CharField(max_length=50)


class Order(models.Model):
    meal = models.ForeignKey('Menu', on_delete=models.SET_NULL, null=True)
    table_number = models.ForeignKey('Table', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    waiter = models.ForeignKey('Waiter', on_delete=models.SET_NULL, null=True)
    total_price = 0






