from django.db import models
from blog.Models.HistorialCambiosModel import HistorialCambios

class Cursos(models.Model):
    idcursos = models.IntegerField(db_column='idCursos', primary_key=True)  # Field name made lowercase.
    nombre_curso = models.CharField(db_column='Nombre_Curso', max_length=120)  # Field name made lowercase.
    fechainicial_curso = models.DateTimeField(db_column='FechaInicial_Curso')  # Field name made lowercase.
    fechafina_cursol = models.DateTimeField(db_column='FechaFina_Cursol')  # Field name made lowercase.
    link_curso = models.CharField(db_column='Link_Curso', max_length=200)  # Field name made lowercase.
    descripcion_cursol = models.CharField(db_column='Descripcion_Cursol', max_length=450)  # Field name made lowercase.
    historial_cambios_idhistorial_cambios = models.ForeignKey(HistorialCambios, models.DO_NOTHING, db_column='historial_cambios_idhistorial_cambios', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cursos'
