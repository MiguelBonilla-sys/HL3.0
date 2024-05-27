from django.shortcuts import render

def menu_admin(request):
    return render(request, 'blog/AdminMenu.html', {'title': 'Menu Administrador'})