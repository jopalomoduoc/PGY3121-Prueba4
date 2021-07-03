from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Libro, Usuario

class LibroForm(ModelForm):
    ISBN = forms.CharField(label='ISBN',widget=forms.TextInput(attrs={"placeholder": "13 dígitos"}))
    nombreLibro = forms.CharField(label='Nombre Libro')
    descripcion = forms.CharField(label='Descripción')
    class Meta:
        model = Libro
        fields = ['ISBN','nombreLibro','descripcion','categoria',]
    
    # def clean_ISBN(self):
    #     ISBN = self.cleaned_data.get("ISBN")
    #     if not len(ISBN) == 13:
    #         raise forms.ValidationError("ISBN no válido")
    #     return ISBN

class RegistroUsuarioForm(ModelForm):
    correo = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "************"}))
    repeatPassword = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "************"}))
    
    class Meta:
        model = Usuario
        fields = ['correo', 'nombre', 'apellido', 'password', 'repeatPassword','comentario',]
