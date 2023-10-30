from django import forms
from .models import Categoria, Autor, Ingrediente, Receta,PerfilUsuarioRecetas
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.views import PasswordChangeView


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = '__all__'

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'

class BusquedaGlobalForm(forms.Form):
    consulta = forms.CharField(label='Buscar', max_length=100)

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

class CustomUserChangeForm(UserChangeForm): 
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuarioRecetas
        fields = ['avatar']

class CambiarContraseñaView(PasswordChangeView):
    success_url = reverse_lazy('Novelas/inicio.html')
