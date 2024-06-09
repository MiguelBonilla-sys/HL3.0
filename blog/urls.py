from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from blog.Views.MenuView import menu
from blog.Views.CursosView import cursos
from blog.Views.NoticiasView import noticias
from blog.Views.ProyectosView import proyectos
from blog.Views.LoginView import login_view, logout_view
from blog.Views.MenuAdminView import AdminMenuView
from blog.Views.NoticiasAdminView import noticias_admin, delete_noticia, update_noticia
from blog.Views.IntegrantesAdminView import integrantes_admin, delete_integrante, update_integrante
from blog.Views.ProyectosAdminView import proyecto_admin, delete_proyecto, update_proyecto
from blog.Views.CursosAdminView import cursos_admin, delete_curso, update_curso

"""
Este archivo urls.py contiene los patrones de URL para la aplicación de blog 
en el proyecto HL3.0. Define las rutas para varias vistas como menú, cursos,
noticias, proyectos, login_view y vistas de administrador para gestionar cursos, noticias, 
integrantes y proyectos. También incluye rutas para manejar la autenticación, cerrar sesión y 
servir archivos estáticos.
"""


urlpatterns = [
    path('', menu, name='menu'),
    path('menu/', include([
        path('cursos/', cursos, name='cursos'),
        path('noticias/', noticias, name='noticias'),
        path('proyectos/', proyectos, name='proyectos'),
        path('login_view/', login_view, name='login_view'),
    ])),
    path('logout/', logout_view, name='logout'),
    path('audit_log/', AdminMenuView.as_view(), name='audit_log'),

    path('audit_log/cursos_admin/', cursos_admin, name='cursos_admin'),
    path('delete_curso/<int:idcursos>/', delete_curso, name='delete_curso'),
    path('update_curso/<int:idcursos>/', update_curso, name='update_curso'),
    
    path('audit_log/noticias_admin/', noticias_admin, name='noticias_admin'),
    path('delete_noticia/<int:idnoticia>/', delete_noticia, name='delete_noticia'),
    path('update_noticia/<int:idnoticia>/', update_noticia, name='update_noticia'),

    path('audit_log/integrantes_admin/', integrantes_admin, name='integrantes_admin'),
    path('delete_integrante/<int:idintegrantes>/', delete_integrante, name='delete_integrante'),
    path('update_integrante/<int:idintegrantes>/', update_integrante, name='update_integrante'),
    
    path('audit_log/proyecto_admin/', proyecto_admin, name='proyecto_admin'),
    path('delete_proyecto/<int:idproyectos>/', delete_proyecto, name='delete_proyecto'),
    path('update_proyecto/<int:idproyectos>/', update_proyecto, name='update_proyecto'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)