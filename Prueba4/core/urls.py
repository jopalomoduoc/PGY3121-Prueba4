from django.urls import path
from .views import home, libro_lista, form_libro, form_mod_libro, form_del_libro, form_registro_usuario, bienvenida_usuario

urlpatterns = [
    
    path('', home, name="home"),
    path('bienvenida-usuario', bienvenida_usuario, name="bienvenida_usuario"),
    path('libro-lista', libro_lista, name="libro_lista"),
    path('form-libro', form_libro, name="form_libro"),
    path('form-mod-libro/<id>', form_mod_libro, name="form_mod_libro"),
    path('form-del-libro/<id>', form_del_libro, name="form_del_libro"),
    path('form-registro-usuario', form_registro_usuario, name="form_registro_usuario"),    
]
