from django.shortcuts import render

# Create your views here.

from .models import Preferencia, StarTalent, Espectador

def preferencias(request):
    if request.method == 'POST':
        # Aquí manejar la lógica del formulario para crear una nueva preferencia
        pass
    else:
        preferencias = Preferencia.objects.all()
        return render(request, 'experiencias_virtuales_app/preferencias.html', {'preferencias': preferencias})


def star_talent(request):
    if request.method == 'POST':
        # Aquí manejar la lógica del formulario para crear un nuevo StarTalent
        pass
    else:
        star_talents = StarTalent.objects.all()
        return render(request, 'experiencias_virtuales_app/star_talent.html', {'star_talents': star_talents})


def espectadores(request):
    if request.method == 'POST':
        # Aquí manejar la lógica del formulario para crear un nuevo Espectador
        pass
    else:
        espectadores = Espectador.objects.all()
        return render(request, 'experiencias_virtuales_app/espectadores.html', {'espectadores': espectadores})

def home(request):
    return render(request, 'experiencias_virtuales_app/home.html')
