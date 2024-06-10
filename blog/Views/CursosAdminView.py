from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from blog.Models.CursosModel import Cursos
from blog.Forms.Cursosform import CursosForm
from blog.Views.decorators import login_required_with_token


@login_required_with_token
def cursos_admin(request):
    """
    Esta vista maneja la creación de nuevos cursos. Si la solicitud es POST, 
    se valida el formulario y se guarda el nuevo curso. Si la solicitud es GET, 
    se muestra el formulario para crear un nuevo curso.
    """
    if request.method == 'POST':
        form = CursosForm(request.POST)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.creador = request.user
            curso.save()
            return redirect('cursos_admin')
    else:
        form = CursosForm()

    cursos = Cursos.objects.all()
    context = {
        'cursos': cursos,
        'form': form
    }
    return render(request, 'blog/AdminCursos.html', context)


@login_required_with_token
def delete_curso(request, idcursos):
    """
    Esta vista maneja la eliminación de un curso. Se obtiene el curso por su id 
    y luego se elimina. Finalmente, se redirige al usuario a la página de administración de cursos.
    """
    curso = get_object_or_404(Cursos, idcursos=idcursos)
    curso.delete()
    return redirect('cursos_admin')


@login_required_with_token
def update_curso(request, idcursos):
    """
    Esta vista maneja la actualización de un curso. Si la solicitud es POST, 
    se valida el formulario y se actualiza el curso. Si la solicitud es GET, 
    se muestra el formulario para actualizar el curso.
    """
    print("inicia el update")
    cursos = get_object_or_404(Cursos, idcursos=idcursos)
    print("Obtiene el objeto curso")
    print(cursos)
    if request.method == "POST":
        print("Entra al metodo post")
        print(request.POST)  # Imprime los datos recibidos
        form = CursosForm(request.POST, instance=cursos)
        if form.is_valid():
            form.save()
            print("Guarda el curso")
            print(form.errors)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = CursosForm(instance=cursos)
    return render(request, 'nombre_del_template.html', {'form': form})