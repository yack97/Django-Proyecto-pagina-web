from django.urls import path

from primerapp import views

urlpatterns = [
    
    path('', views.home, name="home"),
    path('registro', views.registro, name="registro"),
    path('servicios', views.servicios, name="servicios"),
]