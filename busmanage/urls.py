"""
URL configuration for busmanage project.

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
from django.urls import path
from myapp import views
from myapp.views import listar_clientes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('signup/',  views.signup, name='signup'),
    path('homePage/',  views.homePage, name='homePage'),
    path('logout/',  views.inicio, name='logout'),
    path('inicio/',  views.inicio , name='inicio'),
    path('homePage/Paradas/', views.Paradas, name='Paradas'),
    path('homePage/Paradas2/', views.Paradas2, name='Paradas2'),
    path('homePage/Paradas3/', views.Paradas3, name='Paradas3'),
    path('homePage/Paradas4/', views.Paradas4, name='Paradas4'),
    path('homePage/Paradas5/', views.Paradas5, name='Paradas5'),
    path('homePage/Paradas6/', views.Paradas6, name='Paradas6'),
    path('homePage/Paradas7/', views.Paradas7, name='Paradas7'),
    path('homePage/Paradas8/', views.Paradas8, name='Paradas8'),
    path('homePage/Paradas9/', views.Paradas9, name='Paradas9'),
    path('homePage/Paradas10/', views.Paradas10, name='Paradas10'),
    path('homePage/Paradas11/', views.Paradas11, name='Paradas11'),
    path('homePage/Paradas12/', views.Paradas12, name='Paradas12'),
    path('homePage/Paradas13/', views.Paradas13, name='Paradas13'),
    path('homePage/Paradas14/', views.Paradas14, name='Paradas14'),
    path('homePage/Paradas15/', views.Paradas15, name='Paradas15'),   
    path('Paradas/reserva/', views.reserva, name='reserva'),
    path('buscar_resultados/', views.buscar_resultados, name='buscar_resultados'),   
           
   
]
