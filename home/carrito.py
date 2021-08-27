
class Carrito:
  def __init__(self, request):
    self.request = request
    self.session = request.session
    carrito = self.session.get('carrito')
    if not carrito:
      carrito = self.session['carrito'] = {}
    else:
      self.carrito = carrito


  def agregar(self, producto):
    if str(producto.codigo_producto) not in self.carrito.keys():
      self.carrito[producto.codigo_producto] = {
        'producto_id' : producto.codigo_producto,
        'nombre' : producto.nombre,
        'cantidad' : 1,
        'precio' : str(producto.precio),
        'imagen' : producto.image.url
      }
    else:
      for key, value in self.carrito.items():
        if key == str(producto.codigo_producto):
          value['cantidad'] = value['cantidad'] + 1
          break
          
    self.save()
  
  def guardar(self):
    self.session['carrito'] = self.carrito
    self.session.modified = True

  def eliminar(self, producto):
    producto_id = str(producto.codigo_producto)
    if producto_id in self.carrito:
      del self.carrito[producto_id]
      self.save()

  def decrementar(self, producto):
    for key, value in self.carrito.items():
      if key == str(producto.codigo_producto):
        value['cantidad'] = value['cantidad'] - 1
        if value['cantidad'] < 1:
          self.remove(producto)
        else:
          self.save()
        break
      else:
        print('El producto no existe el carrito')
      
  def limpiar_carrito(self):
    self.session['carrito'] = {}
    self.session.modified = True

