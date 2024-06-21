from django.db import models
from django.contrib.auth.models import User

# Asegúrate de que el modelo Integrante esté correctamente importado
from blog.Models.IntegrantesModel import Integrantes  # Ajusta esta línea según la ubicación real de tu modelo Integrante

class Proyectos(models.Model):
    idproyectos = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=150)
    integrantes_proyecto = models.ManyToManyField(Integrantes, related_name='proyectos')
    fecha_proyecto = models.DateTimeField()
    link_proyecto = models.CharField(max_length=250)
    description_proyecto = models.CharField(max_length=450)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'proyectos'