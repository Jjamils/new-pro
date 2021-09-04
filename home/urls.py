import django
from django.urls import path
from django.urls.conf import include
from .import views

#Importacionses para trabajar imagenes
from django.conf import settings
from django.conf.urls.static import static

#app_name = 'home'
urlpatterns = [
  path('', views.home, name = 'home'),
  path('user/', views.user, name = 'user'),
  path('<int:codigo_producto>/', views.detalles, name = 'detalles'),
  path('carrito/', views.carrito, name = 'carrito'),
  path('pago/', views.pago, name = 'pago')
]

#URL para las imagenes
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
