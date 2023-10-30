from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register
from django.contrib.auth.models import User
from django.contrib.auth.views import *
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

def inicio(request):
    return render(request, 'Aplicacion/inicio.html')

def about(request):
    return render(request, 'Aplicacion/about.html')

# Vistas para Ingredientes
def crear_ingrediente(request):
    if request.method == 'POST':
        form = IngredienteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Aplicacion/inicio.html')  # Redirige a donde desees
    else:
        form = IngredienteForm()
    return render(request, 'Aplicacion/ingrediente_crear.html', {'form': form})

def lista_ingredientes(request):
    ingredientes = Ingrediente.objects.all()
    return render(request, 'Aplicacion/ingredientes_lista.html', {'ingredientes': ingredientes})

def editar_ingrediente(request, nombre_ingrediente):
    ingrediente = get_object_or_404(Ingrediente, nombre=nombre_ingrediente)
    if request.method == 'POST':
        form = IngredienteForm(request.POST, instance=ingrediente)
        if form.is_valid():
            form.save()
            return render(request, 'Aplicacion/inicio.html')  # Redirige a donde desees
    else:
        form = IngredienteForm(instance=ingrediente)
    return render(request, 'Aplicacion/ingrediente_editar.html', {'form': form, 'ingrediente': ingrediente})

def eliminar_ingrediente(request, nombre_ingrediente):
    ingrediente = get_object_or_404(Ingrediente, nombre=nombre_ingrediente)
    if request.method == 'POST':
        ingrediente.delete()
        return render(request, 'Aplicacion/inicio.html')  # Redirige a donde desees
    return render(request, 'Aplicacion/ingrediente_eliminar.html', {'ingrediente': ingrediente})

# Vistas para Autores
def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Aplicacion/inicio.html')  # Redirige a donde desees
    else:
        form = AutorForm()
    return render(request, 'Aplicacion/autor_crear.html', {'form': form})

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'Aplicacion/autores_lista.html', {'autores': autores})

def editar_autor(request, nombre_autor):
    autor = get_object_or_404(Autor, user__username=nombre_autor)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return render(request, 'Aplicacion/inicio.html')  # Redirige a donde desees
    else:
        form = AutorForm(instance=autor)
    return render(request, 'Aplicacion/autor_editar.html', {'form': form, 'autor': autor})

def eliminar_autor(request, nombre_autor):
    autor = get_object_or_404(Autor, user__username=nombre_autor)
    if request.method == 'POST':
        autor.delete()
        return render(request, 'Aplicacion/inicio.html')  # Redirige a donde desees
    return render(request, 'Aplicacion/autor_eliminar.html', {'autor': autor})

# Vistas para Categorías
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Aplicacion/inicio.html')  # Redirige a donde desees
    else:
        form = CategoriaForm()
    return render(request, 'Aplicacion/categoria_crear.html', {'form': form})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'Aplicacion/categorias_lista.html', {'categorias': categorias})

def editar_categoria(request, nombre_categoria):
    categoria = get_object_or_404(Categoria, nombre=nombre_categoria)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return render(request, 'Aplicacion/inicio.html')  # Redirige a donde desees
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'Aplicacion/categoria_editar.html', {'form': form, 'categoria': categoria})

def eliminar_categoria(request, nombre_categoria):
    categoria = get_object_or_404(Categoria, nombre=nombre_categoria)
    if request.method == 'POST':
        categoria.delete()
        return render(request, 'Aplicacion/inicio.html')  # Redirige a donde desees
    return render(request, 'Aplicacion/categoria_eliminar.html', {'categoria': categoria})


# Vistas para Recetas
def crear_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Aplicacion/inicio.html')  # Redirige a donde desees
    else:
        form = RecetaForm()
    return render(request, 'Aplicacion/receta_crear.html', {'form': form})

def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'Aplicacion/recetas_lista.html', {'recetas': recetas})

def editar_receta(request, titulo_receta):
    receta = get_object_or_404(Receta, titulo=titulo_receta)
    if request.method == 'POST':
        form = RecetaForm(request.POST, instance=receta)
        if form.is_valid():
            form.save()
            return render(request, 'Aplicacion/inicio.html')  # Redirige a donde desees
    else:
        form = RecetaForm(instance=receta)
    return render(request, 'Aplicacion/receta_editar.html', {'form': form, 'receta': receta})

def eliminar_receta(request, titulo_receta):
    receta = get_object_or_404(Receta, titulo=titulo_receta)
    if request.method == 'POST':
        receta.delete()
        return render(request, 'Aplicacion/inicio.html')  # Redirige a donde desees
    return render(request, 'Aplicacion/receta_eliminar.html', {'receta': receta})

from .models import Receta, Autor, Categoria, Ingrediente

# Vista para la búsqueda global
def busqueda_global(request):
    resultados = None
    consulta = ''
    
    if request.method == 'POST':
        form = BusquedaGlobalForm(request.POST)
        if form.is_valid():
            consulta = form.cleaned_data['consulta']
            resultados = {
                'recetas': Receta.objects.filter(titulo__icontains=consulta),
                'autores': Autor.objects.filter(user__username__icontains=consulta),
                'categorias': Categoria.objects.filter(nombre__icontains=consulta),
                'ingredientes': Ingrediente.objects.filter(nombre__icontains=consulta),
            }
            
            BusquedaRecetas.objects.create(usuario=request.user, consulta=consulta)  # Guardar la consulta de búsqueda
    else:
        form = BusquedaGlobalForm()
    
    return render(request, 'Aplicacion/resultados_busqueda_global.html', {'resultados': resultados, 'consulta': consulta, 'form': form})

# Vistas de sesiones de usuario
def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, 'Aplicacion/inicio.html')  # Redirige a la página de inicio o donde desees
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')

    else:
        form = LoginForm()
    return render(request, 'Aplicacion/iniciar_sesion.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return render(request, 'Aplicacion/inicio.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después del registro
            return render(request, 'Aplicacion/inicio.html', {'message': 'El nuevo usuario ha sido creado exitosamente!'})
    else:
        form = CustomUserCreationForm()
    return render(request, 'Aplicacion/registro.html', {'form': form})

def perfil(request):
    return render(request, 'Aplicacion/perfil.html')

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'Aplicacion/inicio.html')
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'Aplicacion/editar_perfil.html', {'form': form})

@login_required
def eliminar_perfil(request):
    if request.method == 'POST':
        request.user.delete()  # Elimina la cuenta del usuario
        logout(request)  # Cierra la sesión del usuario después de eliminar la cuenta
        return render(request, 'Aplicacion/inicio.html')
    return render(request, 'Aplicacion/eliminar_perfil.html')

@login_required
def edit_avatar(request):
    user_profile, created = PerfilUsuarioRecetas.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return render(request, 'Aplicacion/inicio.html')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'Aplicacion/edit_avatar.html', {'form': form})

class CambiarContraseñaView(PasswordChangeView):
    template_name = 'Aplicacion/cambiar_contraseña.html'  # Reemplaza con la ubicación de tu template
    success_url = reverse_lazy('Aplicacion/inicio.html')  # Reemplaza con la URL de redirección después del cambio de contraseña

    def form_valid(self, form):
        messages.success(self.request, 'Tu contraseña ha sido cambiada exitosamente.')
        return super().form_valid(form)


def blog(request):
    recetas = Receta.objects.all()  # Obtén todas las recetas o filtra según tu lógica
    context = {'recetas': recetas}
    return render(request, 'Aplicacion/blog.html', context)