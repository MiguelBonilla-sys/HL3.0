from django.shortcuts import render, redirect, get_object_or_404
from blog.Models.NoticiasModel import Noticias
from blog.Forms.NoticiasForm import NoticiasForm
from blog.Views.decorators import login_required_with_token

@login_required_with_token
def noticias_admin(request):
    if request.method == 'POST':
        form = NoticiasForm(request.POST)
        if form.is_valid():
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
    noticias = get_object_or_404(Noticias, id=idnoticia)
    noticias.delete()
    return redirect('noticias_admin')

@login_required_with_token
def update_noticia(request, idnoticia):
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