from django.shortcuts import render
from blog.Models.IntegrantesModel import Integrantes
from itertools import cycle

def menu(request):
    integrantes = list(Integrantes.objects.filter(estado=True))
    integrantes_ciclicos = cycle(integrantes)
    integrantes_groups = [list(next(integrantes_ciclicos) for _ in range(4)) for _ in range(0, len(integrantes), 4)]
    return render(request, 'blog/menu.html', {'title': 'Menu', 'integrantes_groups': integrantes_groups})