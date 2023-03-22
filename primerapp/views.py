from django.shortcuts import render
from django.http import HttpResponse

# a total five viewa
def home(request):

    return render(request, "primerapp/home.html")

def registro(request):

    return render(request, "primerapp/registro.html")

def servicios(request):
    
    return render(request, "primerapp/servicios.html")

    