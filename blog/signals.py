from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from blog.Models.HistorialCambiosModel import HistorialCambios
from blog.Models.IntegrantesModel import Integrantes
from blog.Models.ProyectosModel import Proyectos
from blog.Models.NoticiasModel import Noticias
from blog.Models.CursosModel import Cursos
from django.utils import timezone


# Registra los cambios para modelos específicos
@receiver(post_save, sender=Cursos)
@receiver(post_save, sender=Integrantes)
@receiver(post_save, sender=Noticias)
@receiver(post_save, sender=Proyectos)
def log_changes(sender, instance, created, **kwargs):
    user = instance.last_modified_by  # Suponiendo que tienes un campo para el usuario que hizo la última modificación
    table_name = sender.__name__
    action = "ADD" if created else "UPDATE"

    HistorialCambios.objects.create(
        idusuario=user,
        tabla_afectada=table_name,
        id_registro_afectado=instance.pk,
        campo_modificado="N/A",
        valor_anterior="N/A",
        valor_nuevo=str(instance),
        fecha_hora_cambio=timezone.now()
    )

@receiver(post_delete, sender=Cursos)
@receiver(post_delete, sender=Integrantes)
@receiver(post_delete, sender=Noticias)
@receiver(post_delete, sender=Proyectos)
def log_deletion(sender, instance, **kwargs):
    user = instance.last_modified_by  # Suponiendo que tienes un campo para el usuario que hizo la última modificación
    table_name = sender.__name__

    HistorialCambios.objects.create(
        idusuario=user,
        tabla_afectada=table_name,
        id_registro_afectado=instance.pk,
        campo_modificado="N/A",
        valor_anterior=str(instance),
        valor_nuevo="N/A",
        fecha_hora_cambio=timezone.now()
    )
