from django.shortcuts import render

def noticias(request):
    return render(request, 'blog/menuNoticias.html', {'title': 'Noticias'})