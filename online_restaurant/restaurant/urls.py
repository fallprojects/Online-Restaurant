from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('menu',MenuView)
router.register('check_order',MenuToOrderView)
router.register('register', RegisterLoginView)


urlpatterns = [
    path('',include(router.urls)),
    path('check_order/',include(router.urls)),
    path('orders/', OrderView.as_view(), name='orders'),
    path('update_orders/<int:pk>/', UpdateOrder.as_view(), name='updateorders'),
    path('delete_orders/<int:pk>/',UDOrderView.as_view(),name='delete-order'),
    path('register/', include(router.urls), name='register'),
    path('login/', AccountLoginView.as_view(), name='login'),


]
