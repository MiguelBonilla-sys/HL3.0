from django.shortcuts import render

def cursos(request):
    return render(request, 'blog/menuCursos.html', {'title': 'Cursos'})