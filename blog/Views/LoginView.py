from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            print(f"Token for {user.username}: {token.key}")  # Imprimir el token en la consola
            response = redirect('menu_admin')
            response.set_cookie('token', token.key)  # Almacena el token en una cookie
            return response
        else:
            return render(request, 'blog/login.html', {'error': 'Credenciales incorrectas'})
    else:
        return render(request, 'blog/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if username and password and email:
            if User.objects.filter(username=username).exists():
                return render(request, 'blog/register.html', {'error': 'El nombre de usuario ya existe'})
            user = User.objects.create_user(username, email, password)
            return redirect('login_view')
        else:
            return render(request, 'blog/register.html', {'error': 'Todos los campos son obligatorios'})
    else:
        return render(request, 'blog/register.html')
