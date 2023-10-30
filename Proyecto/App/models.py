from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField()
    redes_sociales = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre

class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField(Ingrediente)
    instrucciones = models.TextField()
    tiempo_preparacion = models.PositiveIntegerField()
    porciones = models.PositiveIntegerField()
    
    def __str__(self):
        return self.titulo

class BusquedaRecetas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    consulta = models.TextField()
    fecha_consulta = models.DateTimeField(auto_now_add=True)

class PerfilUsuarioRecetas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username

