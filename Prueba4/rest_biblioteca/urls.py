from django.urls import path
from rest_biblioteca.views import lista_bibliotecas, detalle_biblioteca
##from rest_biblioteca.viewslogin import login

urlpatterns =[
    path('lista_bibliotecas', lista_bibliotecas, name="lista_bibliotecas"),
    path('detalle_biblioteca/<id>', detalle_biblioteca, name="detalle_biblioteca"),
   ## path('login', login, name="login"),
]