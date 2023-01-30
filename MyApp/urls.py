from django.urls import path
from MyApp import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('buscar/', views.buscar),

    path('login', views.login_request, name="Login"),
    path('register', Signup.as_view(), name='Register'),
    path('logout', LogoutView.as_view(template_name='MyApp/logout.html'), name='Logout'),
    path('editarPerfil', UsuarioEdicion.as_view(), name='EditarPerfil'),
    path('cambioPass/', CambioPass.as_view(), name='cambioPass'),
    path('cambioPassOk/' , views.pass_ok, name='passOk'),
    path('olvidePass/' , views.olvidePass, name='olvidePass'),
    path('contacto/' , views.contacto, name='contacto'),
    path('contactoOk/' , views.contactoOk, name='contactoOk'),
    path('comentarioOk/' , views.comentarioOk, name='comentarioOk'),

    path('about/', views.about, name='About'),

#  Subir Juego
    path('videojuegoCreacion/', VideojegoCreacion.as_view(), name='Crear'),
    path('videojuegoCreacionOk/', views.videojuegoCreacionOk, name='videojuegoCreacionOk'),
    

# Accion
    path('listaAccion/', AccionLista.as_view(), name='Accion'),
    path('detalleAccion/<int:pk>/', AccionDetalle.as_view(), name='detalleAccion'),
    path('editarAccion/<int:pk>/', AccionUpdate.as_view(), name='editarAccion'),
    path('eliminarAccion/<int:pk>/', AccionDelete.as_view(), name='eliminarAccion'),
    path('detalleAccion/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

# Aventura
    path('listaAventura/', AventuraLista.as_view(), name='Aventura'),
    path('detalleAventura/<int:pk>/', AventuraDetalle.as_view(), name='detalleAventura'),
    path('editarAventura/<int:pk>/', AventuraUpdate.as_view(), name='editarAventura'),
    path('eliminarAventura/<int:pk>/', AventuraDelete.as_view(), name='eliminarAventura'),
    path('detalleAventura/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

# Estrategia
    path('listaEstrategia/', EstrategiaLista.as_view(), name='Estrategia'),
    path('detalleEstrategia/<int:pk>/', EstrategiaDetalle.as_view(), name='detalleEstrategia'),
    path('editarEstrategia/<int:pk>/', EstrategiaUpdate.as_view(), name='editarEstrategia'),
    path('eliminarEstrategia/<int:pk>/', EstrategiaDelete.as_view(), name='eliminarEstrategia'),
    path('detalleEstrategia/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

# Rol
    path('listaRol/', RolLista.as_view(), name='Rol'),
    path('detalleRol/<int:pk>/', RolDetalle.as_view(), name='detalleRol'),
    path('editarRol/<int:pk>/', RolUpdate.as_view(), name='editarRol'),
    path('eliminarRol/<int:pk>/', RolDelete.as_view(), name='eliminarRol'),
    path('detalleRol/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

# Simulacion
    path('listaSimulacion/', SimulacionLista.as_view(), name='Simulacion'),
    path('detalleSimulacion/<int:pk>/', SimulacionDetalle.as_view(), name='detalleSimulacion'),
    path('editarSimulacion/<int:pk>/', SimulacionUpdate.as_view(), name='editarSimulacion'),
    path('eliminarSimulacion/<int:pk>/', SimulacionDelete.as_view(), name='eliminarSimulacion'),
    path('detalleSimulacion/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

# Otro
    path('listaOtro/', OtroLista.as_view(), name='Otro'),
    path('detalleOtro/<int:pk>/', OtroDetalle.as_view(), name='detalleOtro'),
    path('editarOtro/<int:pk>/', OtroUpdate.as_view(), name='editarOtro'),
    path('eliminarOtro/<int:pk>/', OtroDelete.as_view(), name='eliminarOtro'),
    path('detalleOtro/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario')
]
