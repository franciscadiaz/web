"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from anuncios import views as anuncios_views
from django.conf import settings
from django.conf.urls.static import static
from empresa import views as empresa_views
from portfolio import views as portfolio_views
#from galeria import views as galeria_views
#from inicio import views as inicio_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', anuncios_views.anuncios_list, name = 'anuncios_list'),
    path('', include('sendemail.urls')),
    path('empresas/', empresa_views.empresas_list, name = 'empresas_list'),
    path('portfolio/', portfolio_views.portfolio, name="portfolio" ),
    #path('galeria/', galeria_views.galeria, name="galeria"),
    #path('inicio/', inicio_views.inicio),
]

if settings.DEBUG:    # este codigo se pone en modo local, cuando se trabaja en un servidor directamente no se pone 
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)