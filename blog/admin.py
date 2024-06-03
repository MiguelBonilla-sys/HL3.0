from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

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

# Asignar permisos al grupo de admin (todos los permisos)
for perm in Permission.objects.all():
    admin_group.permissions.add(perm)
