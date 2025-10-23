from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['compania', 'telefono', 'producto', 'precios', 'entregas', 'licencia_permisos']
        widgets = {
            'compania': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'producto': forms.TextInput(attrs={'class': 'form-control'}),
            'precios': forms.NumberInput(attrs={'class': 'form-control'}),
            'entregas': forms.TextInput(attrs={'class': 'form-control'}),
            'licencia_permisos': forms.TextInput(attrs={'class': 'form-control'}),
        }