from django.shortcuts import render, redirect, get_object_or_404
from blog.Models.ProyectosModel import Proyectos
from blog.Models.IntegrantesModel import Integrantes
from blog.Models.ProyectosIntegrantesModel import ProyectosIntegrantesProyecto
from blog.Forms.ProyectosForm import ProyectosForm
from blog.Views.decorators import login_required_with_token
from django.db import transaction

@login_required_with_token
def proyecto_admin(request):
    if request.method == 'POST':
        form = ProyectosForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                proyecto = form.save(commit=False)
                proyecto.creador = request.user
                proyecto.save()
                form.save_m2m()  # Guarda las relaciones Many-to-Many

                # Nuevo código para asociar integrantes
                integrantes_ids = request.POST.getlist('integrantes_proyecto')  # Asume que 'integrantes_proyecto' es el nombre del campo en el formulario
                for integrante_id in integrantes_ids:
                    integrante = get_object_or_404(Integrantes, idintegrantes=integrante_id)  # Usar idintegrantes en lugar de id
                    ProyectosIntegrantesProyecto.objects.create(proyectos=proyecto, integrantes=integrante)

                return redirect('proyecto_admin')
    else:
        form = ProyectosForm()
    
    proyectos = Proyectos.objects.all()
    return render(request, 'blog/AdminProyectos.html', {'form': form, 'proyectos': proyectos})

@login_required_with_token
def delete_proyecto(request, idproyectos):
    proyecto = get_object_or_404(Proyectos, idproyectos=idproyectos)
    proyecto.delete()
    return redirect('proyecto_admin')

@login_required_with_token
def update_proyecto(request, idproyectos):
    proyecto = get_object_or_404(Proyectos, idproyectos=idproyectos)
    if request.method == 'POST':
        form = ProyectosForm(request.POST, instance=proyecto)
        if form.is_valid():
            with transaction.atomic():
                proyecto = form.save(commit=False)
                proyecto.creador = request.user
                ProyectosIntegrantesProyecto.objects.filter(proyectos=proyecto).delete()
                proyecto.save()
                form.save_m2m()  # Guarda las relaciones Many-to-Many

                # Nuevo código para asociar integrantes
                integrantes_ids = request.POST.getlist('integrantes_proyecto')  # Asume que 'integrantes_proyecto' es el nombre del campo en el formulario
                for integrante_id in integrantes_ids:
                    # Asegúrate de usar el campo correcto para buscar el integrante, por ejemplo, 'idintegrantes' si ese es el nombre correcto del campo.
                    integrante = get_object_or_404(Integrantes, idintegrantes=integrante_id)
                    ProyectosIntegrantesProyecto.objects.create(proyectos=proyecto, integrantes=integrante)

                return redirect('proyecto_admin')
        # Si el formulario no es válido, se continúa al renderizado del formulario con los errores.
    else:
        form = ProyectosForm(instance=proyecto)
    # Este render se ejecuta si el método no es POST o si el formulario es inválido.
    return render(request, 'blog/update_proyecto.html', {'form': form, 'proyecto': proyecto})