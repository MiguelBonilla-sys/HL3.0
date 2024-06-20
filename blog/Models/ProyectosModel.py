from django.db import models
from django.contrib.auth.models import User

class Proyectos(models.Model):
    idproyectos = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(db_column='nombre_proyecto', max_length=150)
    intengrantes_proyecto = models.CharField(db_column='intengrantes_proyecto', max_length=450)
    fecha_proyecto = models.DateTimeField(db_column='fecha_proyecto')
    link_proyecto = models.CharField(db_column='link_proyecto', max_length=250)
    description_proyecto = models.CharField(db_column='description_proyecto', max_length=450)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'proyectos'