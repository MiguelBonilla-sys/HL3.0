from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    """
    Esta vista maneja el proceso de inicio de sesión.
    Si el método de la solicitud es POST, intenta autenticar al usuario.
    Si el usuario es autenticado con éxito, se elimina cualquier token existente, se crea uno nuevo,
    se imprime en la consola y se almacena en una cookie.
    Si la autenticación falla, se muestra un mensaje de error.
    Si el método de la solicitud no es POST, simplemente se muestra la página de inicio de sesión.
    """
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
    """
    Esta vista maneja el proceso de cierre de sesión.
    Si el usuario está autenticado, se elimina su token, se cierra su sesión,
    se elimina la cookie con el token y se le redirige a la página de inicio de sesión.
    Si el usuario no está autenticado, simplemente se le redirige a la página de inicio de sesión.
    """
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
