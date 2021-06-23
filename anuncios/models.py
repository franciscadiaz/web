from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class Anuncio(models.Model): #creamos la clase Anuncio
    STATUS_CHOICES = (          #definimos los estados
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
)
    titulo = models.CharField(max_length=150, verbose_name="Título")
    texto = RichTextField(verbose_name="Contenido")
    #autor = models.CharField(max_length=150, verbose_name="Periodista")
    imagen = models.ImageField(null=True, upload_to="images", verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última edición")
    estado = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='borrador')
    class Meta: #Creamos la clase metadatos
        verbose_name="Noticia"
        verbose_name_plural="Noticias"
        ordering = ('-created',) #Ordena por fecha
    def __str__(self): # función que devuelve el titulo
        return self.titulo
