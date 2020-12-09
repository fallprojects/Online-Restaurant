from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('', CustomerRegisterViewset)

urlpatterns = [
    path('register/',include(router.urls)),
    path('delivery_orders/', OrderToDeliveryView.as_view(), name='delivery-order'),

]