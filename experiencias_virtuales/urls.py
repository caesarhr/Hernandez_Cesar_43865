"""
URL configuration for experiencias_virtuales project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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


# experiencias_virtuales/urls.py
from django.contrib import admin
from django.urls import path, include
from experiencias_virtuales_app import views

urlpatterns = [
    # Rutas para el panel de administración
    path('admin/', admin.site.urls),

    # Rutas para las vistas de la aplicación "experiencias_virtuales_app"
    path('home/',views.home, name='home'), #Ruta para la vista "home"
    path('preferencias/', views.preferencias, name='preferencias'),
    path('star_talent/', views.star_talent, name='star_talent'),
    path('espectadores/', views.espectadores, name='espectadores'),
]

