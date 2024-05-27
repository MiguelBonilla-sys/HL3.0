from django.shortcuts import render,redirect
from  blog.Models.UsuariosModel import Usuario

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Usuario.objects.get(nombre=username)
            if user.contraseña == password:
                request.session['user_id'] = user.idusuario
                request.session['username'] = user.nombre
                return redirect('menu_admin')
            else:
                return render(request, 'blog/login.html', {'error': 'Contraseña incorrecta'})
        except Usuario.DoesNotExist:
            return render(request, 'blog/login.html', {'error': 'Usuario no existe'})
    else:
        return render(request, 'blog/login.html')