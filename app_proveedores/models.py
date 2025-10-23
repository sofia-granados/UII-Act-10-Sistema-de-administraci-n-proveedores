from django.db import models

class Proveedor(models.Model):
    compania = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    producto = models.CharField(max_length=100)
    precios = models.DecimalField(max_digits=10, decimal_places=2)
    entregas = models.CharField(max_length=100)  # o DateField si son fechas
    licencia_permisos = models.CharField(max_length=100)
    
    def __str__(self):
        return self.compania