from django.contrib import admin

# Register your models here.

from .models import Anuncio
#admin.site.register(Anuncio)

class AnunciosAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Anuncio, AnunciosAdmin)