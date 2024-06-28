from django.shortcuts import render
from rest_framework import viewsets
from .serializer import VehiculoSerializer
from .models import vehiculo

# Create your views here.

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset= vehiculo.objects.all()                                                                       
    serializer_class= VehiculoSerializer


