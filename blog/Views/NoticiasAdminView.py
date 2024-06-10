from django.shortcuts import render, redirect, get_object_or_404
from blog.Models.NoticiasModel import Noticias
from blog.Forms.NoticiasForm import NoticiasForm
from .decorators import login_required_with_token

@login_required_with_token
def noticias_admin(request):
    """
    Vista de administración de noticias. Si el método de la solicitud es POST, 
    se valida el formulario de noticias y se guarda una nueva noticia con el 
    usuario de la solicitud como creador. Si el método de la solicitud no es POST, 
    se inicializa un formulario de noticias vacío. En ambos casos, se renderiza 
    la plantilla 'blog/AdminNoticias.html' con todas las noticias y el formulario.
    """
    if request.method == 'POST':
        form = NoticiasForm(request.POST)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.creador = request.user
            form.save()
            return redirect('noticias_admin')
    else:
        form = NoticiasForm()

    noticias = Noticias.objects.all()
    context = {
        'noticias': noticias,
        'form': form
    }

    return render(request, 'blog/AdminNoticias.html', context)

@login_required_with_token
def delete_noticia(request, idnoticia):
    """
    Vista para eliminar una noticia. Se obtiene la noticia por su idnoticia y 
    se elimina. Luego se redirige al usuario a la vista de administración de noticias.
    """
    noticia = get_object_or_404(Noticias, idnoticia=idnoticia)
    noticia.delete()
    return redirect('noticias_admin')

@login_required_with_token
def update_noticia(request, idnoticia):
    """
    Vista para actualizar una noticia. Se obtiene la noticia por su idnoticia. 
    Si el método de la solicitud es POST, se valida el formulario de noticias 
    y se actualiza la noticia. Si el método de la solicitud no es POST, se inicializa 
    el formulario de noticias con la noticia existente. En ambos casos, se renderiza 
    la plantilla 'blog/UpdateNoticia.html' con el formulario y la noticia.
    """
    noticia = get_object_or_404(Noticias, idnoticia=idnoticia)
    if request.method == 'POST':
        form = NoticiasForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('noticias_admin')
    else:
        form = NoticiasForm(instance=noticia)
    
    context = {
        'form': form,
        'noticia': noticia
    }
    return render(request, 'blog/UpdateNoticia.html', context)