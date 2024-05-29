from django.urls import path
from blog.Views.MenuView import menu
from blog.Views.CursosView import cursos
from blog.Views.NoticiasView import noticias
from blog.Views.ProyectosView import proyectos
from blog.Views.LoginView import login_view
from blog.Views.MenuAdminView import menu_admin

from django.conf import settings
from django.conf.urls.static import static

from blog.Views.NoticiasAdminView import noticias_admin, delete_noticia, update_noticia
from blog.Views.IntegrantesAdminView import integrantes_admin, delete_integrante
from blog.Views.ProyectosAdminView import proyecto_admin, delete_proyecto
from blog.Views.CursosAdminView import cursos_admin, delete_curso
urlpatterns = [
    path('', menu, name='menu'),
    path('menu.html', menu, name='menu'),
    path('menuCursos.html', cursos, name='cursos'),
    path('menuNoticias.html', noticias, name='noticias'),
    path('menuProyect.html', proyectos, name='proyectos'),
    path('login.html', login_view, name='login_view'),
    path('AdminMenu.html', menu_admin, name='menu_admin'),

    path('AdminNoticias.html', noticias_admin, name='noticias_admin'),  # Cambiado aquí
    path('delete_noticia/<int:idnoticia>/', delete_noticia, name='delete_noticia'),
    path('update_noticia/<int:idnoticia>/', update_noticia, name='update_noticia'),

    path('AdminIntegrantes.html', integrantes_admin, name='integrantes_admin'),
    path('delete_integrante/<int:idintegrantes>/', delete_integrante, name='delete_integrante'),

    path('AdminProyectos.html', proyecto_admin, name='proyecto_admin'),
    path('delete_proyecto/<int:idproyectos>/', delete_proyecto, name='delete_proyecto'),

    path('AdminCursos.html', cursos_admin, name='cursos_admin'),
    path('delete_curso/<int:idcursos>/', delete_curso, name='delete_curso'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
