from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.html import format_html

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(upload_to="portfolio", verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def get_image(self):
        if self.image:
            return format_html('<img src="{}" style="width: 120px"; \
                height: 120px"/>',format(self.image.url))
        else:
            return '(Sin imagen)'

    get_image.short_description = "miniatura"
    
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title

