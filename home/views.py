from django.shortcuts import render
from .models import Producto
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm

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



def pago():
  context = {}
  return render(request, 'home/checkout.html', context)

#Registro de usuario
def user(request):
  form = UserCreationForm()
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      user = form.changed_data.get('username')
      password_login = form.changed_data.get('password1')
      usuario = authenticate(username=user, password=password_login)
      login(request, usuario)
      messages.success(request, 'Cuenta creada' + user)
      return redirect(to='/Quilitienda')
  else:
    form = UserCreationForm()
  context = {'form': form}
  return render(request, 'user.html', context)



