from django.db import models
from blog.Models.HistorialCambiosModel import HistorialCambios

class Integrantes(models.Model):
    idintegrantes = models.AutoField(db_column='idIntegrantes', primary_key=True)  # Field name made lowercase.
    nombre_integrante = models.CharField(max_length=135)
    semestre = models.CharField(db_column='Semestre', max_length=45)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=90)  # Field name made lowercase.
    link_git = models.CharField(db_column='Link_Git', max_length=190)  # Field name made lowercase.
    imagen = models.TextField(db_column='Imagen')  # Field name made lowercase.
    historial_cambios_idhistorial_cambios = models.ForeignKey(HistorialCambios, models.DO_NOTHING, db_column='historial_cambios_idhistorial_cambios', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'integrantes'