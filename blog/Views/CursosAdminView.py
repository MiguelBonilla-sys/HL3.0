from django.shortcuts import render, redirect, get_object_or_404
from blog.Models.CursosModel import Cursos
from blog.Forms.CursosForm import CursosForm

def cursos_admin(request):
    if request.method == 'POST':
        form = CursosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos_admin')
    else:
        form = CursosForm()

    cursos = Cursos.objects.all()
    context = {
        'cursos': cursos,
        'form': form
    }
    return render(request, 'blog/AdminCursos.html', context)


def delete_curso(request, idcursos):
    curso = get_object_or_404(Cursos, idcursos=idcursos)
    curso.delete()
    return redirect('cursos_admin')