from django.shortcuts import render, redirect
from blog.Models.IntegrantesModel import Integrantes
from blog.Forms.IntegrantesForm import IntegrantesForm
from django.shortcuts import get_object_or_404
import base64

def integrantes_admin(request):
    if request.method == 'POST':
        form = IntegrantesForm(request.POST, request.FILES)
        if form.is_valid():
            integrante = form.save(commit=False)
            # Si se ha subido una imagen, codifícala en base64
            if 'imagen' in request.FILES:
                imagen = request.FILES['imagen']
                imagen_data = imagen.read()
                imagen_base64 = base64.b64encode(imagen_data).decode()
                integrante.imagen = imagen_base64
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

def delete_integrante(request, idintegrantes):
    integrantes = get_object_or_404(Integrantes, idintegrantes=idintegrantes)
    integrantes.delete()
    return redirect('integrantes_admin')
