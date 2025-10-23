from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Proveedor
from .forms import ProveedorForm


# Create your views here.
def index(request):
    return render(request, 'proveedor/index.html', {
        'proveedores': Proveedor.objects.all()
    })


def view_proveedor(request, id):
    return HttpResponseRedirect(reverse('index'))


def add(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            new_compania = form.cleaned_data['compania']
            new_telefono = form.cleaned_data['telefono']
            new_producto = form.cleaned_data['producto']
            new_precios = form.cleaned_data['precios']
            new_entregas = form.cleaned_data['entregas']
            new_licencia_permisos = form.cleaned_data['licencia_permisos']

            new_proveedor = Proveedor(
                compania=new_compania,
                telefono=new_telefono,
                producto=new_producto,
                precios=new_precios,
                entregas=new_entregas,
                licencia_permisos=new_licencia_permisos
            )
            new_proveedor.save()
            return render(request, 'proveedor/add.html', {
                'form': ProveedorForm(),
                'success': True
            })
    else:
        form = ProveedorForm()
    return render(request, 'proveedor/add.html', {
        'form': ProveedorForm()
    })


def edit(request, id):
    if request.method == 'POST':
        proveedor = Proveedor.objects.get(pk=id)
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return render(request, 'proveedor/edit.html', {
                'form': form,
                'success': True
            })
    else:
        proveedor = Proveedor.objects.get(pk=id)
        form = ProveedorForm(instance=proveedor)
    return render(request, 'proveedor/edit.html', {
        'form': form
    })


def delete(request, id):
    if request.method == 'POST':
        proveedor = Proveedor.objects.get(pk=id)
        proveedor.delete()
    return HttpResponseRedirect(reverse('index'))