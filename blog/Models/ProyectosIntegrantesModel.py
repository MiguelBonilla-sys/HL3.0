from django.db import models
from blog.Models.IntegrantesModel import Integrantes
from blog.Models.ProyectosModel import Proyectos

class ProyectosIntegrantesProyecto(models.Model):
    proyectos = models.ForeignKey(Proyectos, on_delete=models.DO_NOTHING, db_column='proyectos_id')
    integrante = models.ForeignKey(Integrantes, on_delete=models.DO_NOTHING, db_column='integrantes_id')

    class Meta:
        managed = False
        db_table = 'proyectos_integrantes_proyecto'