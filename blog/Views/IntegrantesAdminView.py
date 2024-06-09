from django.shortcuts import render, redirect
from blog.Models.IntegrantesModel import Integrantes
from blog.Forms.IntegrantesForm import IntegrantesForm
from django.shortcuts import get_object_or_404
import base64
from blog.Views.decorators import login_required_with_token
from django.http import JsonResponse

@login_required_with_token
def integrantes_admin(request):
    """
    Vista para administrar los integrantes. Si el método de la solicitud es POST, 
    se intenta guardar un nuevo integrante. Si el método de la solicitud es GET, 
    se muestra el formulario para crear un nuevo integrante.
    """
    if request.method == 'POST':
        form = IntegrantesForm(request.POST, request.FILES)
        if form.is_valid():
            integrante = form.save(commit=False)
            if 'imagen' in request.FILES:
                imagen = request.FILES['imagen']
                imagen_data = imagen.read()
                imagen_base64 = base64.b64encode(imagen_data).decode()
                integrante.imagen = imagen_base64
            integrante.creador = request.user  # Asignar el usuario actual como creador
            integrante.save()
            return redirect('integrantes_admin')
        else:
            print("ERROR: " + str(form.errors))
    else:
        form = IntegrantesForm()

    integrantes = Integrantes.objects.all()
    context = {
        'integrantes': integrantes,
        'form': form
    }
    return render(request, 'blog/AdminIntegrantes.html', context)

@login_required_with_token
def delete_integrante(request, idintegrantes):
    """
    Vista para eliminar un integrante. Se intenta obtener el integrante con el 
    id proporcionado y luego se elimina. Finalmente, se redirige al usuario a la 
    vista de administración de integrantes.
    """
    integrante = get_object_or_404(Integrantes, idintegrantes=idintegrantes)
    integrante.delete()
    return redirect('integrantes_admin')

@login_required_with_token
def update_integrante(request, idintegrantes):
    """
    Vista para actualizar un integrante. Si el método de la solicitud es POST, 
    se intenta actualizar el integrante con el id proporcionado. Si el método de 
    la solicitud es GET, se devuelve un error.
    """
    integrante = get_object_or_404(Integrantes, idintegrantes=idintegrantes)
    if request.method == "POST":
        form = IntegrantesForm(request.POST, request.FILES, instance=integrante)
        if form.is_valid():
            integrante = form.save(commit=False)
            if 'imagen' in request.FILES:
                imagen = request.FILES['imagen']
                imagen_data = imagen.read()
                imagen_base64 = base64.b64encode(imagen_data).decode()
                integrante.imagen = imagen_base64
            else:
                integrante.imagen = Integrantes.objects.get(idintegrantes=idintegrantes).imagen
            integrante.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})