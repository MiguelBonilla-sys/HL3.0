from django.shortcuts import render, redirect
from blog.Models.ProyectosModel import Proyectos
from blog.Forms.ProyectosForm import ProyectosForm
from django.shortcuts import get_object_or_404
from blog.Views.decorators import login_required_with_token

@login_required_with_token
def proyecto_admin(request):
    if request.method == 'POST':
        form = ProyectosForm(request.POST)
        if form.is_valid():
            form.save()
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
            form.save()
            return redirect('proyecto_admin')
    else:
        form = ProyectosForm(instance=proyecto)
    
    return render(request, 'blog/AdminProyectos.html', {'form': form})