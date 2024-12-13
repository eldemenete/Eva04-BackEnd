"""
URL configuration for Eva04BackEnd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from ReservasApp import views

# Crear el router
router = DefaultRouter()

# Registra el ViewSet con el router
router.register(r'reservas', views.ReservaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservas/', views.lista_reservas, name='lista_reservas'),  # Tu vista basada en función (FBV)
    path('api/', include(router.urls)), 
    ]
