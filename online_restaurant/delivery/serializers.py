from rest_framework import serializers

from .models import Address, OrderToDelivery


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
