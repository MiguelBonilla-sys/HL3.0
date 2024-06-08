from django.db import models
from django.contrib.auth.models import User

class Cursos(models.Model):
    idcursos = models.AutoField(db_column='idCursos', primary_key=True)  # Field name made lowercase.
    nombre_curso = models.CharField(db_column='Nombre_Curso', max_length=120)  # Field name made lowercase.
    fechainicial_curso = models.DateTimeField(db_column='FechaInicial_Curso')  # Field name made lowercase.
    fechafina_cursol = models.DateTimeField(db_column='FechaFina_Curso')  # Field name made lowercase.
    link_curso = models.CharField(db_column='Link_Curso', max_length=200)  # Field name made lowercase.
    descripcion_cursol = models.CharField(db_column='Descripcion_Curso', max_length=450)  # Field name made lowercase.
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'cursos'
