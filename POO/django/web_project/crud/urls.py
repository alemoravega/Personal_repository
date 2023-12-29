from django.urls import path
from crud import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("lee", views.lee, name="lee"),
    path("escribe", views.escribe, name="escribe"),
    path("mod-usuario", views.mod_usuario, name="mod-usuario"),
    path("hacer-envio", views.formulario_carga, name="hacer-envio"),

]