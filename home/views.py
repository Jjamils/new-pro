from home.carrito import Carrito
from django.core import paginator
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import Producto
from .forms import CompradorForm, UserCreationForm
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UsernameField
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404

#Funcion para listar los productos y condicion para realizar la busqueda por productos
def home (request):
  total_productos = Producto.objects.all()
  buscar =request.GET.get('barra_busqueda')
  #Codigo para pagiador
  page = request.GET.get('page', 1)
  
  try:
    paginator = Paginator(total_productos, 4)
    total_productos = paginator.page(page)
  except:
    raise Http404
  #Codigo para la barra de busqueda
  if buscar:
    total_productos = Producto.objects.filter(
      Q(nombre__icontains = buscar) |
      Q(marca__icontains = buscar) |
      Q(descripcion__icontains = buscar) |
      Q(categoria__nombre__icontains = buscar)
    ).distinct()
  
  data = {
    'entity': total_productos,
    'paginator':paginator
  }

  return render(request, 'home/home.html', data)

#Funcion para visualizar detalles de producto en su propio html
def detalles(request, codigo_producto):
  product_object = Producto.objects.get(codigo_producto= codigo_producto)
  return render(request, 'home/detalles.html', {'product_object': product_object})

def pago(request):
  context = {}
  return render(request, 'home/pago.html', context)

#Registro de usuario
def user(request):
  form = UserCreationForm()
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      user = form.cleaned_data.get('username')
      password_login = form.changed_data.get('password1')
      usuario = authenticate(username=user, password=password_login)
      login(request, usuario)
      messages.success(request, 'Cuenta creada' + user)
      return redirect(to='/home')
  else:
    form = UserCreationForm()
  context = {'form': form}
  return render(request, 'home/user.html', context)

def logout(request):
  return render(request, 'home.html')

def registro(request):
  data = {
    'form' : CompradorForm()
  }

  if request.method == 'POST':
    formulario = CompradorForm(data = request.POST)
    if formulario.is_valid():
      formulario.save()
      user = authenticate(username = formulario.cleaned_data['username'],
      password = formulario.cleaned_data['password1'])
      login(request, user)
      messages.success(request, 'Te has registrado correctamente!')
      return redirect(to = 'home')
    data['form'] = formulario

  return render(request, 'registration/registro.html', data)

def carrito(request):
  productos = Producto.objects.all()
  context = {'productos': productos}
  
  return render(request, 'home/carrito.html', context)

def agregar_carrito(request, producto_id):
  carrito = Carrito(request)
  productos = Producto.objects.get(id = producto_id)
  carrito.agregar(productos)
  return redirect(to= home)

def eliminar_carrito(request, producto_id):
  carrito = Carrito(request)
  producto = Producto.objects.get(producto_id = producto_id)
  carrito.eliminar(producto)
  return redirect(to= home)

def restar_carrito(request, producto_id):
  carrito = Carrito(request)
  producto = Producto.objects.get(producto_id = producto_id)
  carrito.restar(producto)
  return redirect(to= home)

def limpiar_carrito(request):
  carrito = Carrito(request)
  carrito.limpiar_carrito()
  return redirect(to= home)