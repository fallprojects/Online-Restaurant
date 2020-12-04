from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('delivery_orders/', OrderToDeliveryView.as_view(), name='delivery-order'),

]