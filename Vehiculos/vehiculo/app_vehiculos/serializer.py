from rest_framework import serializers
from .models import vehiculo

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model=vehiculo
        fields='__all__'
        
