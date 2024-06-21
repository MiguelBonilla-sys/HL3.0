from django.shortcuts import render, redirect
from blog.Models.ProyectosModel import Proyectos
from blog.Models.IntegrantesModel import Integrantes
from blog.Forms.ProyectosForm import ProyectosForm
from django.shortcuts import get_object_or_404
from blog.Views.decorators import login_required_with_token

@login_required_with_token
def proyecto_admin(request):
    """
    Esta vista maneja la creación de nuevos proyectos y la asociación de integrantes a estos proyectos.
    Si el método de la solicitud es POST, valida el formulario y guarda el nuevo proyecto en la base de datos,
    luego asocia los integrantes seleccionados. Si el método de la solicitud no es POST, simplemente renderiza
    el formulario de proyectos.
    """
    if request.method == 'POST':
        form = ProyectosForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.creador = request.user
            proyecto.save()
            # Verificar si 'integrantes_proyecto' está presente en cleaned_data y no está vacío
            integrantes_ids = form.cleaned_data.get('integrantes_proyecto', [])
            if integrantes_ids:
                for integrante_id in integrantes_ids:
                    integrante = Integrantes.objects.get(idintegrantes=integrante_id)
                    proyecto.integrantes.add(integrante)
            return redirect('proyecto_admin')
    else:
        form = ProyectosForm()
    proyectos = Proyectos.objects.all()
    return render(request, 'blog/AdminProyectos.html', {'form': form, 'proyectos': proyectos})

@login_required_with_token
def delete_proyecto(request, idproyectos):
    """
    Esta vista maneja la eliminación de proyectos. Obtiene el proyecto por su id y lo elimina.
    Luego redirige al usuario a la página de administración de proyectos.
    """
    proyecto = get_object_or_404(Proyectos, idproyectos=idproyectos)
    proyecto.delete()
    return redirect('proyecto_admin')

@login_required_with_token
def update_proyecto(request, idproyectos):
    """
    Esta vista maneja la actualización de proyectos. Obtiene el proyecto por su id y, si el método de la solicitud
    es POST, actualiza el proyecto con los datos del formulario. Independientemente del método de la solicitud,
    redirige al usuario a la página de administración de proyectos.
    """
    proyecto = get_object_or_404(Proyectos, idproyectos=idproyectos)
    if request.method == 'POST':
        form = ProyectosForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('proyecto_admin')
    else:
        ProyectosForm(instance=proyecto)    
        return redirect('proyecto_admin')