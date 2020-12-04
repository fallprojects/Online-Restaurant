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
        fields = ['id', 'order', 'amounts', 'meal', 'total_price', 'sales']

    def get_total_price(self, order):
        total_price = 0

        if self.data['sales']:
            check_order = MenuToOrder.objects.filter(order=order.order)
            for order in check_order:
                total_price += order.meal.price * order.amounts
                sales = order.total_price - order.total_price * order.percent // 100
                return sales
            return total_price












