from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import Location
import folium
from datetime import datetime, timedelta
from django.urls import reverse
from .models import Asiento, Reserva
from django.contrib.auth.decorators import login_required
from myapp.models import Asiento
from django.db.models import Q
from django.contrib import messages



# Create your views here.


def home(request):
    return render(request, 'home.html', {
        'form': UserCreationForm
    })


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            # register. user
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('homePage')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Username already exist'
                })
    return render(request, 'signup.html', {
        'form': UserCreationForm,
        "error": 'password do not match'
    })


def homePage(request):
    locations = Location.objects.all()
    initialMap = folium.Map(location=[40.564546, -3.608776], zoom_start=18)
    for location in locations:
        coordinates = (location.latitude, location.longitude)
        folium.Marker(coordinates, popup=location.name).add_to(initialMap)

    context = {'map': initialMap._repr_html_(), 'locations': Location}
    return render(request, 'homePage.html',  {'map': initialMap._repr_html_(), 'locations': locations})


def signout(request):
    logout(request)
    return (redirect('homePage'))


def inicio(request):
    if request.method == 'GET':
        return render(request, 'inicio.html', {
            'form': AuthenticationForm

        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password1'])

        if user is None:
            return render(request, 'inicio.html', {
                'form': AuthenticationForm,
                'error': 'Username or password incorrect'
            })
        else:
            login(request, user)
            return redirect('homePage')


def Paradas(request):

    return render(request, 'Paradas.html')


def Paradas2(request):

    return render(request, 'Paradas2.html')


def Paradas3(request):

    return render(request, 'Paradas3.html')


def Paradas4(request):

    return render(request, 'Paradas4.html')


def Paradas5(request):

    return render(request, 'Paradas5.html')


def Paradas6(request):

    return render(request, 'Paradas6.html')


def Paradas7(request):

    return render(request, 'Paradas7.html')

def Paradas8(request):

    return render(request, 'Paradas8.html')

def Paradas9(request):

    return render(request, 'Paradas9.html')

def Paradas10(request):

    return render(request, 'Paradas10.html')

def Paradas11(request):

    return render(request, 'Paradas11.html')

def Paradas12(request):

    return render(request, 'Paradas12.html')

def Paradas13(request):

    return render(request, 'Paradas13.html')

def Paradas14(request):

    return render(request, 'Paradas14.html')

def Paradas15(request):

    return render(request, 'Paradas15.html')


def reserva(request):
   
    if request.method == 'POST':
        
        numero_asiento = request.POST.get('numero_asiento')
       
        
        try:
               
                asiento = Asiento.objects.get(numero=numero_asiento)
               
                if asiento.disponible:
                    
                    asiento.disponible = False
                    asiento.save()
                    mensaje = f"¡asiento {numero_asiento} reservado con éxito!"
                else:
                    mensaje = f"El asiento {numero_asiento} ya está reservado."
        except Asiento.DoesNotExist:
                mensaje = f"El asiento {numero_asiento} no existe."
        else:
            mensaje = "El número de asiento no es válido."

        
        asientos = Asiento.objects.all()
        return render(request, 'reserva.html', {'asientos': asientos, 'mensaje': mensaje})
    else:
        
        asientos = Asiento.objects.all()
        messages.success(request, "Reserva realizada con éxito")
        return render(request, 'reserva.html', {'asientos': asientos})
    


def detalle_reserva(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    return render(request, 'detalle_reserva.html', {'reserva': reserva})





def listar_clientes(request):
      busqueda = request.POST.get('search')
      paradas = Location.objects.all()  # Usamos Location en lugar de Parada
    
      if busqueda:
        paradas = Location.filter(
            Q(name__icontains=busqueda) | 
            Q(address__icontains=busqueda)
        ).distinct() 
    
        return render(request, 'homePage.html', {'paradas': paradas})
    
def buscar_resultados(request):
    
    condicion = True  
    
    if condicion:
       
        return render(request, 'Paradas.html')
    else:
       
        return render(request, 'Paradas2.html')
    
    