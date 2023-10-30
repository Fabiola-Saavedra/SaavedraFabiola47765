from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('about/', views.about, name="about"),
    
    # URLs para Autores
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/crear/', views.crear_autor, name='crear_autor'),
    path('autores/editar/<nombre_autor>/', views.editar_autor, name='editar_autor'),
    path('autores/eliminar/<nombre_autor>/', views.eliminar_autor, name='eliminar_autor'),
   
    # URLs para Categorías
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('categorias/editar/<nombre_categoria>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<nombre_categoria>/', views.eliminar_categoria, name='eliminar_categoria'),

    # URLs para Ingredientes
    path('ingredientes/', views.lista_ingredientes, name='lista_ingredientes'),
    path('ingredientes/crear/', views.crear_ingrediente, name='crear_ingrediente'),
    path('ingredientes/editar/<nombre_ingrediente>/', views.editar_ingrediente, name='editar_ingrediente'),
    path('ingredientes/eliminar/<nombre_ingrediente>/', views.eliminar_ingrediente, name='eliminar_ingrediente'),

    # URLs para Recetas
    path('recetas/', views.lista_recetas, name='lista_recetas'),
    path('recetas/crear/', views.crear_receta, name='crear_receta'),
    path('recetas/editar/<titulo_receta>/', views.editar_receta, name='editar_receta'),
    path('recetas/eliminar/<titulo_receta>/', views.eliminar_receta, name='eliminar_receta'),
    
    # URLs para Blog
    path('blog/', views.blog, name='blog'),

    # URLs para Buscar
    path('buscar/', views.busqueda_global, name='buscar_global'),

    # URLs para Usuarios
    path('registro/', views.register, name='registro'),
    path('iniciarsesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfileditar/', views.editar_perfil, name='editar_perfil'),
    path('perfileditar/edit-avatar/', views.edit_avatar, name='edit_avatar'),
    path('perfileliminar/', views.eliminar_perfil, name='eliminar_perfil'),
    path('cerrarsesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('cambiarcontrasena', views.CambiarContraseñaView.as_view(), name='cambiar_contrasena'),
]
