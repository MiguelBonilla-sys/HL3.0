from django.shortcuts import render, redirect, get_object_or_404
from blog.Models.NoticiasModel import Noticias
from blog.Forms.NoticiasForm import NoticiasForm
from blog.Views.decorators import login_required_with_token
import base64
from django.http import JsonResponse
from django.core.paginator import Paginator

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
        form = NoticiasForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            if 'imagen_noticia' in request.FILES:
                imagen = request.FILES['imagen_noticia']
                imagen_data = imagen.read()
                imagen_base64 = base64.b64encode(imagen_data).decode()
                noticia.imagen_noticia = imagen_base64  # Asegurarse de que esto se asigna correctamente
            noticia.creador = request.user
            noticia.save()
            return redirect('noticias_admin')
    else:
        form = NoticiasForm()

    noticias = Noticias.objects.all().order_by('idnoticia')
    paginator = Paginator(noticias, 5)
    page_number = request.GET.get('page')
    page_noticias = paginator.get_page(page_number)

    context = {
        'noticias': page_noticias,
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
    la plantilla 'blog/AdminNoticias.html' con el formulario y la noticia.
    """
    noticia = get_object_or_404(Noticias, idnoticia=idnoticia)
    if request.method == "POST":
        form = NoticiasForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            noticia = form.save(commit=False)
            if 'imagen_noticia' in request.FILES:
                imagen_N = request.FILES['imagen_noticia']
                imagen_data = imagen_N.read()
                imagen_base64 = base64.b64encode(imagen_data).decode()
                noticia.imagen_noticia = imagen_base64
            else:
                noticia.imagen_noticia = Noticias.objects.get(idnoticia=idnoticia).imagen_noticia
            

            noticia.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})