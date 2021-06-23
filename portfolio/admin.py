from django.contrib import admin
from .models import Portfolio
# Register your models here.

class PortfolioApp(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Portfolio, PortfolioApp)

