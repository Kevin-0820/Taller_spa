from django.contrib import admin
from django.urls import path,include
from app_vehiculos import views
from rest_framework import routers

router= routers.DefaultRouter()
router.register('vehiculos',views.VehiculoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
]

