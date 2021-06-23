from django.shortcuts import render
from .models import Empresa
# Create your views here.

def empresas_list(request):
    empresas = Empresa.objects.filter(estado= "publicado")
    return render(request,
                  "empresas.html",
                  {"empresas": empresas})