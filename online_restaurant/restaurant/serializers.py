from rest_framework import serializers
from .models import *


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'




    # def update(self, instance, validated_data):
    #     meal = validated_data.pop('meal')
    #     # instance.meal = validated_data.get('meal',instance.meal)
    #     Order.objects.update(**meal)
    #     return instance

class MenuToOrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField('get_total_price')


    class Meta:
        model = MenuToOrder
        fields = ['id', 'order', 'amounts', 'meal', 'total_price', 'sales', 'percent']

    def get_total_price(self, order):
        total_price = 0
        sales = 0
        if 1:
            check_order = MenuToOrder.objects.filter(order=order.order)
            for order in check_order:
                total_price = order.meal.price * order.amounts
                sales = total_price - total_price * order.percent // 100

            return sales


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


    def create(self, validated_data):
        password = self.validated_data.get('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
