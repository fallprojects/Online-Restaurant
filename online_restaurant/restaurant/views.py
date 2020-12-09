from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class MenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['menu_types']


class OrderView(APIView):

    def get(self, *args, **kwargs):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


class MenuToOrderView(viewsets.ModelViewSet):
    queryset = MenuToOrder.objects.all()
    serializer_class = MenuToOrderSerializer


class UDOrderView(APIView):

    # def put(self,request, *args, **kwargs):
    #     order = Order.objects.get(id=kwargs['pk'])
    #     serializer = OrderSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'data':'success'})

    def delete(self, request, *args, **kwargs):
        order = Order.objects.get(id=kwargs['pk'])
        order.delete()
        return Response({'data':"success"})


class UpdateOrder(generics.UpdateAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class SalesView(viewsets.ModelViewSet):
    queryset = MenuToOrder.objects.all()
    serializer_class = MenuToOrderSerializer



class RegisterLoginView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AccountLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request':request}
                                           )
        if not serializer.is_valid():
            return Response({'User not found'})
        user = serializer.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
        return Response({'token':token.key})














