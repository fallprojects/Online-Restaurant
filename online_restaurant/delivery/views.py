from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from rest_framework import viewsets, status
from .serializers import *

# Create your views here.


class OrderToDeliveryView(APIView):

    def get(self, *args, **kwargs):
        orders = OrderToDelivery.objects.all()
        serializer = OrderToDeliverySerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        serializer = OrderToDeliverySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

