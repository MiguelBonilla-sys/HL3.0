from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            Token.objects.filter(user=user).delete()  # Elimina el token existente
            token = Token.objects.create(user=user)  # Crea un nuevo token
            print(f"Token for {user.username}: {token.key}")  # Imprimir el token en la consola
            response = redirect('audit_log')
            response.set_cookie('token', token.key)  # Almacena el token en una cookie
            return response
        else:
            return render(request, 'blog/login.html', {'error': 'Credenciales incorrectas'})
    else:
        return render(request, 'blog/login.html')


def logout_view(request):
    user = request.user
    if user.is_authenticated:
        print(f"Logging out user: {user.username}")
        Token.objects.filter(user=user).delete()  # Elimina el token del usuario
        logout(request)  # Desautentica al usuario
        response = redirect('login_view')
        response.delete_cookie('token')  # Elimina la cookie con el token
        print("Token cookie deleted")
        return response
    else:
        print("User is not authenticated")
        return redirect('login_view')
