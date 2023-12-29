from django.http import HttpResponse
from django.shortcuts import render, redirect
from crud.funciones import leer, escribir, modificar_usuario, ingresar_carga
import datetime


def home(request):
    return HttpResponse


def lee(request):
    if request.POST:
        data = request.POST.dict()
        usuario = data.get("usuario")
        password = data.get("password")
        if leer(usuario, password):
            return render(request, "crud/opciones.html", )
        else:
            return render(request, "crud/acceso-denegado.html", )
    return render(request, "crud/lee.html", )


def escribe(request):
    if request.POST:
        data = request.POST.dict()
        usuario = data.get("usuario")
        password = data.get("password")
        escribir(usuario, password)
        print(data)
    return render(request, "crud/escribe.html")


def mod_usuario(request):
    if request.POST:
        data = request.POST.dict()
        usuario = data.get("usuario")
        password = data.get("password")
        nueva_password = data.get("nueva_password")
        modificar_usuario(usuario, password, nueva_password)
        print(data)
    return render(request, "crud/mod-usuario.html")


def formulario_carga(request):
    if request.POST:
        data = request.POST.dict()
        destinatario = data.get("destinatario")
        d_origen = data.get("d_origen")
        d_envio = data.get("d_envio")
        peso = data.get("peso")
        volumen = data.get("volumen")
        hoy = datetime.date.today()
        ingresar_carga(destinatario, d_origen, d_envio, peso, volumen, hoy)
        print(data)
    return render(request, "crud/hacer-envio.html")
