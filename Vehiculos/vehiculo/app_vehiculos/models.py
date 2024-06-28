from django.db import models


class vehiculo(models.Model):
    id=models.AutoField(primary_key=True)
    modelo=models.PositiveBigIntegerField()
    marca=models.CharField(max_length=30)
    Referencia=models.CharField(max_length=100)
    Fecha=models.DateTimeField(auto_now=True)
    Valor=models.PositiveIntegerField()
    
    class meta:
       db_table='vehiculo'
       
