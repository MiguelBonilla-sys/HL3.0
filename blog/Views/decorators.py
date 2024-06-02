from django.shortcuts import redirect
from django.http import JsonResponse

"""
    Decorador que verifica si el usuario está autenticado y tiene un token válido.
    
    Args:
        view_func (function): La función de vista que se va a decorar.
    
    Returns:
        function: La función decorada que verifica la autenticación y el token.

"""

# Este es un decorador en Python que se utiliza para asegurar que un usuario esté autenticado antes de permitirle acceder a una vista específica.
def login_required_with_token(view_func):
    # Esta es la función envolvente que se llama en lugar de la función de vista original.
    def _wrapped_view(request, *args, **kwargs):
        # Comprueba si el usuario está autenticado. Si no lo está, redirige al usuario a la vista de inicio de sesión.
        if not request.user.is_authenticated:
            return redirect('login_view')
        
        # Intenta obtener un token de las cookies de la solicitud. Si no hay un token, redirige al usuario a la vista de inicio de sesión.
        token = request.COOKIES.get('token')
        if not token:
            return redirect('login_view')

        # Si el usuario está autenticado y tiene un token, llama a la función de vista original con los mismos argumentos y devuelve su resultado.
        return view_func(request, *args, **kwargs)
    
    # El decorador devuelve la función envolvente.
    return _wrapped_view
