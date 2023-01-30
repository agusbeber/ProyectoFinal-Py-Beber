from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import *
from MyApp.forms import UserRegisterForm

@login_required
def inicio(request):
    return render(request, 'MyApp/inicio.html')

def login_request(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        contrasenia = request.POST['password']
        user = authenticate(request, username=usuario, password=contrasenia)
        if user is not None:
            login(request, user)
            return render(request, "MyApp/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
        else:
            return render(request, 'MyApp/login.html', {'error': 'Ups! Credenciales inválidas'})
    return render(request, 'MyApp/login.html')

class Signup(FormView):
    template_name = 'MyApp/signup.html'
    form_class = FormularioSignup
    redirect_autheticated_user = True
    success_url = reverse_lazy('Inicio')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Signup, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('Inicio')
        return super(Signup, self).get(*args, **kwargs)

def olvidePass(request):
    return render(request, 'MyApp/olvidePass.html')

def contacto(request):
    return render(request, 'MyApp/contacto.html')

def contactoOk(request):
    return render(request, 'MyApp/contactoOk.html', {})

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'MyApp/editarPerfil.html'
    success_url = reverse_lazy('Inicio')

    def get_object(self):
        return self.request.user

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre'] 
        videojuego = Videojuego.objects.filter(nombre__icontains=nombre)
        return render(request, "MyApp/inicio.html", {"videojuego":videojuego, "nombre":nombre})
    return render(request, "MyApp/inicio.html"  )

class CambioPass(PasswordChangeView):
    form_class = FormularioCambioPass
    template_name = 'MyApp/cambioPass.html'
    success_url = reverse_lazy('passOk')

def pass_ok(request):
    return render(request, 'MyApp/cambioPassOk.html', {})

    # CREAR VIDEOJUEGO

class VideojegoCreacion(LoginRequiredMixin, CreateView):
    model = Videojuego
    form_class = FormularioNuevoVideojuego
    success_url = reverse_lazy('videojuegoCreacionOk')
    template_name = 'MyApp/videojuegoCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VideojegoCreacion, self).form_valid(form)

def videojuegoCreacionOk(request):
    return render(request, 'MyApp/videojuegoCreacionOk.html', {})

    # ACCIÓN

class AccionLista(LoginRequiredMixin, ListView):
    context_object_name = 'accion'
    queryset = Videojuego.objects.filter(genero__startswith='accion')
    template_name = 'MyApp/listaAccion.html'

class AccionDetalle(LoginRequiredMixin, DetailView):
    model = Videojuego
    context_object_name = 'accion'
    template_name = 'MyApp/detalleAccion.html'

class AccionUpdate(LoginRequiredMixin, UpdateView):
    model = Videojuego
    form_class = ActualizacionVideojuego
    success_url = reverse_lazy('Accion')
    context_object_name = 'accion'
    template_name = 'MyApp/editarAccion.html'

class AccionDelete(LoginRequiredMixin, DeleteView):
    model = Videojuego
    success_url = reverse_lazy('Accion')
    context_object_name = 'accion'
    template_name = 'MyApp/eliminarAccion.html'

    # AVENTURA

class AventuraLista(LoginRequiredMixin, ListView):
    context_object_name = 'aventura'
    queryset = Videojuego.objects.filter(genero__startswith='aventura')
    template_name = 'MyApp/listaAventura.html'

class AventuraDetalle(LoginRequiredMixin, DetailView):
    model = Videojuego
    context_object_name = 'aventura'
    template_name = 'MyApp/detalleAventura.html'

class AventuraUpdate(LoginRequiredMixin, UpdateView):
    model = Videojuego
    form_class = ActualizacionVideojuego
    success_url = reverse_lazy('Aventura')
    context_object_name = 'aventura'
    template_name = 'MyApp/editarAventura.html'

class AventuraDelete(LoginRequiredMixin, DeleteView):
    model = Videojuego
    success_url = reverse_lazy('Aventura')
    context_object_name = 'aventura'
    template_name = 'MyApp/eliminarAventura.html'

    # ESTRATEGIA

class EstrategiaLista(LoginRequiredMixin, ListView):
    context_object_name = 'estrategia'
    queryset = Videojuego.objects.filter(genero__startswith='estrategia')
    template_name = 'MyApp/listaEstrategia.html'

class EstrategiaDetalle(LoginRequiredMixin, DetailView):
    model = Videojuego
    context_object_name = 'estrategia'
    template_name = 'MyApp/detalleEstrategia.html'

class EstrategiaUpdate(LoginRequiredMixin, UpdateView):
    model = Videojuego
    form_class = ActualizacionVideojuego
    success_url = reverse_lazy('Estrategia')
    context_object_name = 'estrategia'
    template_name = 'MyApp/editarEstrategia.html'

class EstrategiaDelete(LoginRequiredMixin, DeleteView):
    model = Videojuego
    success_url = reverse_lazy('Estrategia')
    context_object_name = 'estrategia'
    template_name = 'MyApp/eliminarEstrategia.html'

    # ROL

class RolLista(LoginRequiredMixin, ListView):
    context_object_name = 'rol'
    queryset = Videojuego.objects.filter(genero__startswith='rol')
    template_name = 'MyApp/listaRol.html'

class RolDetalle(LoginRequiredMixin, DetailView):
    model = Videojuego
    context_object_name = 'rol'
    template_name = 'MyApp/detalleRol.html'

class RolUpdate(LoginRequiredMixin, UpdateView):
    model = Videojuego
    form_class = ActualizacionVideojuego
    success_url = reverse_lazy('Rol')
    context_object_name = 'rol'
    template_name = 'MyApp/editarRol.html'

class RolDelete(LoginRequiredMixin, DeleteView):
    model = Videojuego
    success_url = reverse_lazy('Rol')
    context_object_name = 'rol'
    template_name = 'MyApp/eliminarRol.html'

    # SIMULACIÓN

class SimulacionLista(LoginRequiredMixin, ListView):
    context_object_name = 'simulacion'
    queryset = Videojuego.objects.filter(genero__startswith='simulacion')
    template_name = 'MyApp/listaSimulacion.html'

class SimulacionDetalle(LoginRequiredMixin, DetailView):
    model = Videojuego
    context_object_name = 'simulacion'
    template_name = 'MyApp/detalleSimulacion.html'

class SimulacionUpdate(LoginRequiredMixin, UpdateView):
    model = Videojuego
    form_class = ActualizacionVideojuego
    success_url = reverse_lazy('Simulacion')
    context_object_name = 'simulacion'
    template_name = 'MyApp/editarSimulacion.html'

class SimulacionDelete(LoginRequiredMixin, DeleteView):
    model = Videojuego
    success_url = reverse_lazy('Simulacion')
    context_object_name = 'simulacion'
    template_name = 'MyApp/eliminarSimulacion.html'

    # OTRO

class OtroLista(LoginRequiredMixin, ListView):
    context_object_name = 'otro'
    queryset = Videojuego.objects.filter(genero__startswith='otro')
    template_name = 'MyApp/listaOtro.html'

class OtroDetalle(LoginRequiredMixin, DetailView):
    model = Videojuego
    context_object_name = 'otro'
    template_name = 'MyApp/detalleOtro.html'

class OtroUpdate(LoginRequiredMixin, UpdateView):
    model = Videojuego
    form_class = ActualizacionVideojuego
    success_url = reverse_lazy('Otro')
    context_object_name = 'otro'
    template_name = 'MyApp/editarOtro.html'

class OtroDelete(LoginRequiredMixin, DeleteView):
    model = Videojuego
    success_url = reverse_lazy('Otro')
    context_object_name = 'otro'
    template_name = 'MyApp/eliminarOtro.html'

    # COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'MyApp/comentario.html'
    success_url = reverse_lazy('comentarioOk')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

def comentarioOk(request):
    return render(request, 'MyApp/comentarioOk.html', {})

# ABOUT
def about(request):
    return render(request, 'MyApp/about.html', {})