from django.shortcuts import render
from .models import Producto
from django.db.models import Q

#Funcion para listar los productos y condicion para realizar la busqueda por productos

def home (request):
  total_productos = Producto.objects.all()
  item_name =request.GET.get('barra_busqueda')

  if item_name:
    total_productos = Producto.objects.filter(
      Q(nombre__icontains = item_name) |
      Q(descripcion__icontains = item_name)
    ).distinct()
  return render(request, 'home/home.html', {'total_productos': total_productos})

#Funcion para visualizar detalles de producto en su propio html

def detalles(request, codigo_producto):
  product_object = Producto.objects.get(codigo_producto= codigo_producto)
  return render(request, 'home/detalles.html', {'product_object': product_object})



def carrito():
  context = {}
  return render(request, 'home/carrito.html', context)



def checkout():
  context = {}
  return render(request, 'home/checkout.html', context)


