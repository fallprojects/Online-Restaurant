from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('menu',MenuView)

urlpatterns = [

    path('',include(router.urls)),
    path('orders/', OrderView.as_view(), name='orders'),
    path('udorders/<int:pk>/', UDOrderView.as_view(), name='updatedeleteorders'),

]
