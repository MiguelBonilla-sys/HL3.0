from django.db import models
from django.contrib.auth.models import User
from blog.Models.IntegrantesModel import Integrantes

class Proyectos(models.Model):
    idproyectos = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=150)
    fecha_proyecto = models.DateTimeField()
    link_proyecto = models.CharField(max_length=250)
    description_proyecto = models.CharField(max_length=450)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    integrantes = models.ManyToManyField(Integrantes, through='ProyectosIntegrantesProyecto')

    class Meta:
        managed = False
        db_table = 'proyectos'
