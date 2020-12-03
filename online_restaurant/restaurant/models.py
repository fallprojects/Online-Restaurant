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
    price = models.IntegerField(default=0)


    def __str__(self):
        return self.name



class Table(models.Model):
    table_number = models.IntegerField(default=0)


class Waiter(models.Model):
    waiter_name = models.CharField(max_length=50)


class Order(models.Model):
    table_number = models.ForeignKey('Table', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    waiter = models.ForeignKey('Waiter', on_delete=models.SET_NULL, null=True)



class MenuToOrder(models.Model):
    amounts = models.IntegerField(default=0)
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    meal = models.ForeignKey('Menu', on_delete=models.SET_NULL, null=True)
    sales = models.BooleanField()
    percent = models.IntegerField()

