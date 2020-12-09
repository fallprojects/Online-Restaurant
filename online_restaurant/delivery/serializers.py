from rest_framework import serializers

from .models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        password = self.validated_data.get('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class EndPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'endpoint']


class OrderToDeliverySerializer(serializers.ModelSerializer):
    endpoint = EndPointSerializer(many=True)


    class Meta:
        model = OrderToDelivery
        fields = ['id', 'customer', 'order', 'start_date', 'end_date', 'status', 'endpoint']

    def create(self, validated_data):
        endpoints = validated_data.pop('endpoint')
        order = OrderToDelivery.objects.create(**validated_data)
        for endpoint in endpoints:
            Address.objects.create(order=order, **endpoint)
        return order

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        endpoints = validated_data.pop('endpoint')
        for endpoint in endpoints:
            Address.objects.update(**endpoint)
            if endpoint not in endpoints:
                endpoint.delete()
        instance.save()
        return instance
