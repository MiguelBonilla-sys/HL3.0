from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

from blog.Models.CursosModel import Cursos
from blog.Models.IntegrantesModel import Integrantes
from blog.Models.ProyectosModel import Proyectos
from blog.Models.NoticiasModel import Noticias
from blog.Models.AuditLogModel import AuditLog

# Registrar modelos para que aparezcan en el panel de administración
admin.site.register(Cursos)
admin.site.register(Integrantes)
admin.site.register(Proyectos)
admin.site.register(Noticias)
admin.site.register(AuditLog)

# Crear grupos
staff_group, created = Group.objects.get_or_create(name='Staff')
admin_group, created = Group.objects.get_or_create(name='Admin')

# Obtener permisos
content_type = ContentType.objects.get_for_model(User)
add_user_permission = Permission.objects.get(codename='add_user', content_type=content_type)
change_user_permission = Permission.objects.get(codename='change_user', content_type=content_type)

# Asignar permisos al grupo de staff
staff_group.permissions.add(add_user_permission)
staff_group.permissions.add(change_user_permission)

models_to_assign = [Cursos, Integrantes, Noticias, Proyectos, AuditLog]
for model in models_to_assign:
    content_type = ContentType.objects.get_for_model(model)
    permissions = Permission.objects.filter(content_type=content_type)
    for perm in permissions:
        if perm.codename in ['add', 'change', 'delete', 'view']:
            staff_group.permissions.add(perm)
            admin_group.permissions.add(perm)

# Asignar todos los permisos al grupo de admin
admin_group.permissions.set(Permission.objects.all())