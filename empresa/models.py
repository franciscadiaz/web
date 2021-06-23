from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Empresa(models.Model): #creamos la clase Empresa
    STATUS_CHOICES = (          #definimos los estados
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
)
    noticia = models.CharField(max_length=150, verbose_name="Título")
    texto = models.TextField(verbose_name="Contenido")
    autor = models.CharField(max_length=150, verbose_name="Periodista")
    imagen = models.ImageField(null=True, upload_to="images", verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última edición")
    estado = models.CharField(max_length=10, choices=STATUS_CHOICES, default='borrador')
    class Meta: #Creamos la clase metadatos
        verbose_name="Empresa"
        verbose_name_plural="Empresas"
        ordering = ('-created',) #Ordena por fecha
    def __str__(self): # función que devuelve la noticia
        return self.noticia

