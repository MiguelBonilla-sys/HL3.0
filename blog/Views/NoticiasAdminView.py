from django.shortcuts import render, redirect, get_object_or_404
from blog.Models.NoticiasModel import Noticias
from blog.Forms.NoticiasForm import NoticiasForm


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

def delete_noticia(request, idnoticia):
    noticias = get_object_or_404(Noticias, idnoticia=idnoticia)
    noticias.delete()
    return redirect('noticias_admin')

def update_noticia(request, idnoticia):
    noticia = get_object_or_404(Noticias, idnoticia=idnoticia)
    if request.method == "POST":
        print(request.POST)  # Imprime los datos de la solicitud POST
        form = NoticiasForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()  # This saves the form to the database
            return redirect('noticias_admin')
        else:
            print(form.errors)  # Print form errors for debugging purposes
    else:
        form = NoticiasForm(instance=noticia)
    return render(request, 'blog/AdminNoticias.html', {'form': form})
