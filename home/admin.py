from django.contrib import admin
from .models import Administrador, Categoria, Comprador, Producto, Pedido, Envio

admin.site.register(Administrador)
admin.site.register(Categoria)
admin.site.register(Comprador)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Envio)