class Carrito:
  def __init__(self, request):
    self.request = request
    self.session = request.session
    carrito = self.session['carrito']
    if not carrito:
      self.session['carrito'] = {}
      self.carrito = self.session['carrito']
    else:
      self.carrito = carrito


  def agregar(self, productos):
    id = str(productos.codigo_producto)
    if id not in self.carrito.keys():
      self.carrito[id] = {
        'codigo' : productos.codigo_producto,
        'nombre' : productos.nombre,
        'cantidad' : 1,
        'acomulado' : str(productos.precio),
        'imagen' : productos.image.url
      }
    else:
      self.carrito[id] ['cantidad'] += 1
      self.carrito[id] ['acomulado'] += productos.precio
      #for key, value in self.carrito.items():
        #if key == str(producto.codigo_producto):
         # value['cantidad'] = value['cantidad'] + 1
         # break
    self.guardar_carrito()     
    #self.save()
  
  def guardar_carrito(self):
    self.session['carrito'] = self.carrito
    self.session.modified = True

  def eliminar(self, producto):
    producto_id = str(producto.codigo_producto)
    if producto_id in self.carrito:
      del self.carrito[producto_id]
      self.guardar_carrito()

  def restar(self, producto):
    producto_id = str(producto.codigo_producto)
    if producto_id in self.carrito.keys():
      self.carrito[id] ['cantidad'] -= 1
      self.carrito[id] ['acomulado'] -= producto.precio
      if self.carrito[id] ['cantidad'] < 1: 
        self.eliminar(producto)
        self.guardar_carrito

    #for key, value in self.carrito.items():
     # if key == str(producto.codigo_producto):
      #  value['cantidad'] = value['cantidad'] - 1
       # if value['cantidad'] < 1:
        #  self.remove(producto)
        #else:
         # self.save()
        #break
      #else:
       # print('El producto no existe el carrito')
      
  def limpiar_carrito(self):
    self.session['carrito'] = {}
    self.session.modified = True

