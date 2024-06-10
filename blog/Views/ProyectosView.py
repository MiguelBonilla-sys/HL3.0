from django.shortcuts import render

def proyectos(request):
    return render(request, 'blog/menuProyect.html', {'title': 'Proyectos'})