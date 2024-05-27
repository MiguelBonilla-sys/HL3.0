from django.shortcuts import render

def menu(request):
    return render(request, 'blog/menu.html', {'title': 'Menu'})