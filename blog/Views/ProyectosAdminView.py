from django.shortcuts import render, redirect
from blog.Models.ProyectosModel import Proyectos
from blog.Forms.ProyectosForm import ProyectosForm
from django.shortcuts import get_object_or_404

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

def delete_proyecto(request, idproyectos):
    proyecto = get_object_or_404(Proyectos, idproyectos=idproyectos)
    proyecto.delete()
    return redirect('proyecto_admin')

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