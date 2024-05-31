from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from blog.Models.CursosModel import Cursos
from blog.Forms.Cursosform import CursosForm

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





def update_curso(request, idcursos):
    # Intenta obtener el curso con el idcursos proporcionado
    cursos = get_object_or_404(Cursos, idcursos=idcursos)

    # Si la solicitud es un POST, intenta actualizar el curso
    if request.method == "POST":
        # Crea un formulario con los datos de la solicitud y el curso existente como instancia
        form = CursosForm(request.POST, instance=cursos)

        # Si el formulario es válido, guarda los cambios y devuelve una respuesta JSON con el estado 'success'
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})

        # Si el formulario no es válido, devuelve una respuesta JSON con el estado 'error' y los errores del formulario
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})

    # Si la solicitud no es un POST, crea un formulario para el curso existente
    else:
        form = CursosForm(instance=cursos)

    # Devuelve el formulario como respuesta
    return render(request, 'nombre_del_template.html', {'form': form})
