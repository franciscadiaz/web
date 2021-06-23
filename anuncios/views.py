from django.shortcuts import render
from .models import Anuncio

# Create your views here.

#from django.http import HttpResponse

def anuncios_list (request):
    anuncios = Anuncio.objects.filter(estado="publicado")
    return render(request,"anuncios.html", {"anuncios":anuncios})

