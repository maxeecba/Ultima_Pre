from django.shortcuts import render
from .models import Cliente
# Create your views here.
def index(request):
    clientes = Cliente.objects.all()#esta funcion trae todos los registros de cliente (es una instancia de cliente)
    return render(request,"Cliente/index.html",{"contexto" : clientes})#de esta forma le pasamos todo el contenido de la instancia cliente
