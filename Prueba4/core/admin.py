from django.contrib import admin
from .models import Categoria, Libro, Usuario
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Libro)
admin.site.register(Usuario)