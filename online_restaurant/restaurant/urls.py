from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('menu',MenuView)
router.register('check_order',MenuToOrderView)

urlpatterns = [

    path('',include(router.urls)),
    path('check_order/',include(router.urls)),
    path('orders/', OrderView.as_view(), name='orders'),
    path('update_orders/<int:pk>/', UpdateOrder.as_view(), name='updateorders'),
    path('delete_orders/<int:pk>/',UDOrderView.as_view(),name='delete-order'),







]
