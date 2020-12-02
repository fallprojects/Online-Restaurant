from rest_framework import serializers
from .models import *


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    meal = MenuSerializer()
    class Meta:
        model = Order
        fields = '__all__'



    def update(self, instance, validated_data):
        meal = validated_data.pop('meal')
        # instance.meal = validated_data.get('meal',instance.meal)
        Order.objects.update(**meal)
        return instance







