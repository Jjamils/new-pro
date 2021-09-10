from django.conf.urls.static import static
from django.db import models
from django.contrib.auth.models import User

class Administrador(models.Model):
  imagen = models.ImageField(upload_to= 'images', null= True, blank= False, verbose_name= 'Foto')
  documento = models.CharField(max_length= 15, primary_key= True, verbose_name= 'Cedula')
  nombre = models.CharField(max_length= 60, verbose_name= 'Nombres y Apellidos')
  contraseña = models.CharField(max_length= 15, verbose_name= 'Contraseña')

  def __str__(self):
    return self.nombre


class Categoria(models.Model):
  codigo = models.AutoField(primary_key= True)
  nombre = models.CharField(max_length= 30, verbose_name= 'Categoria')
  descripcion = models.TextField(max_length= 100, verbose_name= 'Descripcion de Categoria')

  def __str__(self):
    return self.nombre


class Comprador (models.Model):
  imagen = models.ImageField(upload_to= 'images', null= True, blank= False, verbose_name= 'Foto')
  tipo_documentacion = [('TI', 'Tarjeta de identidad'), ('CC', 'Cedula de ciudadania'), ('CE', 'Cedula de extranjeria')]
  tipo_documento = models.CharField(max_length= 2, choices= tipo_documentacion, default= 'CC', verbose_name= 'Tipo de documeto')
  documento = models.CharField(max_length = 15, primary_key = True, verbose_name='No. de documento')
  contraseña = models.CharField(default=1234, max_length= 15, verbose_name= 'Contraseña')
  nombres = models.CharField(max_length = 60, verbose_name= 'Nombres')
  apellidos = models.CharField(max_length = 60, verbose_name= 'Apellidos')
  direccion_envio = models.CharField(max_length = 100, verbose_name= 'Direccion de envio')
  telefono = models.CharField(max_length = 15, verbose_name= 'Telefonono')
  email = models.EmailField(verbose_name='Correo electronico')

  def nombre_completo(self):
    return "{} {}".format(self.nombres, self.apellidos)

  def __str__(self):
    return self.nombre_completo()


class Producto (models.Model):
  codigo_producto = models.AutoField(primary_key = True)
  imagen = models.ImageField(upload_to= 'images', null= False, blank= False, verbose_name= 'Imagen')
  nombre = models.CharField(max_length=30, verbose_name= 'Nombre de prodcto')
  marca = models.CharField(max_length=30, default='', verbose_name= 'Marca')
  descripcion = models.TextField(max_length=300, verbose_name= 'Descripcion')
  precio = models.DecimalField(max_digits= 20, decimal_places= 2, default= 0.00, verbose_name= 'Precio')
  inventario = [('S', 'En stock'), ('N', 'Agotado')
  ]
  disponibilidad = models.CharField(max_length= 1, choices= inventario, default= 'S', verbose_name= 'Disponibilidad')
  stock = models.IntegerField(verbose_name= 'Cantidad en inventario')
  cantidad = models.IntegerField(default= 0, null= True, blank= True)
  categoria = models.ForeignKey(Categoria, null= False, blank= False, on_delete= models.CASCADE)

  def __str__(self):
    return self.nombre


class Pedido(models.Model):
  codigo_pedido = models.AutoField(primary_key= True)
  opciones_estado = [('P', 'Pendiente'),('C', 'Confirmado')
  ]
  estado = models.CharField(max_length= 1, choices= opciones_estado, default= 'P')
  fecha = models.DateField(auto_now_add= True)
  comprador = models.OneToOneField(Comprador, null= False, blank= False, on_delete= models.CASCADE)
  producto = models.ForeignKey(Producto, null= False, blank= False, on_delete= models.CASCADE)

  def __str__(self):
    return "{} {}".format(self.codigo_pedido, self.fecha.strftime('%A %d %m %Y %H:%M:%S'))
    

class Envio(models.Model):
  cod_envio = models.AutoField(primary_key= True)
  pedido = models.OneToOneField(Pedido, null= False, blank= False, on_delete= models.CASCADE)

  def __str__(self):
    txt = "( {} )"
    return txt.format(self.cod_envio)



"""from django.db import models


class Usuario_comprador(models.Model):
  imagen = models.CharField(max_length= 300, null= True, blank= True, verbose_name= 'Foto')
  documento = models.CharField(max_length= 15, primary_key= True, verbose_name= 'Cedula')
  nombre = models.CharField(max_length= 60, verbose_name= 'Nombres y Apellidos')
  contraseña = models.CharField(max_length= 15, verbose_name= 'Contraseña')
  
  def __str__(self):
    return self.nombre


class Administrador(models.Model):
  imagen = models.CharField(max_length= 300, null= True, blank= False, verbose_name= 'Foto')
  documento = models.CharField(max_length= 15, primary_key= True, verbose_name= 'Cedula')
  nombre = models.CharField(max_length= 60, verbose_name= 'Nombres y Apellidos')
  contraseña = models.CharField(max_length= 15, verbose_name= 'Contraseña')

  def __str__(self):
    return self.nombre


class Categoria(models.Model):
  codigo = models.AutoField(primary_key= True)
  nombre = models.CharField(max_length= 30, verbose_name= 'Categoria')
  descripcion = models.TextField(max_length= 100, verbose_name= 'Descripcion de Categoria')

  def __str__(self):
    return self.nombre


class Comprador (models.Model):
  documento = models.CharField(max_length = 15, primary_key = True, verbose_name='No. Cedula')
  nombres = models.CharField(max_length = 60, verbose_name= 'Nombres')
  apellidos = models.CharField(max_length = 60, verbose_name= 'Apellidos')
  direccion_envio = models.CharField(max_length = 100, verbose_name= 'Direccion de envio')
  telefono = models.CharField(max_length = 15, verbose_name= 'Telefonono')
  email = models.EmailField(verbose_name='Correo electronico')
  #Cuando ya se igresen valores modifica la foreign key a valor null= False
  usuario_comprador = models.ForeignKey(Usuario_comprador, null= True, blank= False, on_delete= models.CASCADE)

  def nombre_completo(self):
    return "{} {}".format(self.nombres, self.apellidos)

  def __str__(self):
    return self.nombre_completo()


class Producto (models.Model):
  codigo_producto = models.AutoField(primary_key = True)
  imagen = models.CharField(max_length= 300, null= True, blank= False, verbose_name= 'Imagen')
  item = models.CharField(max_length=30, verbose_name= 'Nombre de prodcto')
  descripcion = models.TextField(max_length=300, verbose_name= 'Descripcion')
  precio = models.IntegerField(verbose_name= 'Precio')
  inventario = [('S', 'Si'), ('N', 'No')
  ]
  stock = models.CharField(max_length= 1, choices= inventario, default= 'S')
  categoria = models.ForeignKey(Categoria, null= False, blank= False, on_delete= models.CASCADE)

  def __str__(self):
    return self.item


class Pedido(models.Model):
  codigo_pedido = models.AutoField(primary_key= True)
  opciones_estado = [('P', 'Pendiente'),('C', 'Confirmado')
  ]
  estado = models.CharField(max_length= 1, choices= opciones_estado, default= 'P')
  fecha = models.DateField(auto_now_add= True)
  comprador = models.ForeignKey(Comprador, null= False, blank= False, on_delete= models.CASCADE)
  producto = models.ForeignKey(Producto, null= False, blank= False, on_delete= models.CASCADE)

  def __str__(self):
    txt = "( {} )"
    return txt.format (self.fecha.strftime('%A %d %m %Y %H:%M:%S'))

  def __str__(self):
    return self.codigo_pedido

    

class Envio(models.Model):
  cod_envio = models.AutoField(primary_key= True)
  pedido = models.ForeignKey(Pedido, null= False, blank= False, on_delete= models.CASCADE)

  def __str__(self):
      return self.cod_envio

"""