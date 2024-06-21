from django.shortcuts import render, redirect
from blog.Models.IntegrantesModel import Integrantes
from blog.Models.ProyectosIntegrantesModel import ProyectosIntegrantesProyecto
from blog.Forms.IntegrantesForm import IntegrantesForm
from django.shortcuts import get_object_or_404
import base64
from blog.Views.decorators import login_required_with_token
from django.http import JsonResponse

from django.core.paginator import Paginator

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
            
            # Aquí conviertes el valor del formulario a booleano
            estado_formulario = request.POST.get('estado')
            if estado_formulario == '1':
                integrante.estado = True
            elif estado_formulario == '0':
                integrante.estado = False
            
            integrante.creador = request.user  # Asignar el usuario actual como creador
            integrante.save()
            return redirect('integrantes_admin')
        else:
            print("ERROR: " + str(form.errors))
    else:
        form = IntegrantesForm()
    
    if request.is_ajax():
        term = request.GET.get('term', '')
        integrantes_query = Integrantes.objects.filter(nombre_integrante__icontains=term).order_by('idintegrantes')[:10]
        return JsonResponse([{'id': integrante.idintegrantes, 'text': integrante.nombre_integrante} for integrante in integrantes_query], safe=False)

    integrantes = Integrantes.objects.order_by('idintegrantes')
    paginator = Paginator(integrantes, 4)
    page_number = request.GET.get('page')
    page_integrantes = paginator.get_page(page_number)

    context = {
        'integrantes': page_integrantes,
        'form': form
    }
    return render(request, 'blog/AdminIntegrantes.html', context)



@login_required_with_token
def delete_integrante(request, idintegrantes):
    integrante = get_object_or_404(Integrantes, idintegrantes=idintegrantes)
    # Asegúrate de que el nombre del campo sea correcto
    ProyectosIntegrantesProyecto.objects.filter(integrante=idintegrantes).delete()
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
            
            # Aquí conviertes el valor del formulario a booleano
            estado_formulario = request.POST.get('estado')
            if estado_formulario == '1':
                integrante.estado = True
            elif estado_formulario == '0':
                integrante.estado = False

            integrante.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})