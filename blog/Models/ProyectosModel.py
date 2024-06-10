from django.db import models
from django.contrib.auth.models import User


class Proyectos(models.Model):
    idproyectos = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(db_column='Nombre_Proyecto', max_length=150)  # Field name made lowercase.
    intengrantes_proyecto = models.CharField(db_column='Intengrantes_Proyecto', max_length=450)  # Field name made lowercase.
    fecha_proyecto = models.DateTimeField(db_column='Fecha_Proyecto')  # Field name made lowercase.
    link_proyecto = models.CharField(db_column='Link_Proyecto', max_length=250)  # Field name made lowercase.
    description_proyecto = models.CharField(db_column='Description_Proyecto', max_length=450)  # Field name made lowercase.
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'proyectos'
