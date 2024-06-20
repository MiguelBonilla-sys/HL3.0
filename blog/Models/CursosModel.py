from django.db import models
from django.contrib.auth.models import User

class Cursos(models.Model):
    idcursos = models.AutoField(db_column='idcursos', primary_key=True)  # Field name made lowercase.
    nombre_curso = models.CharField(db_column='nombre_curso', max_length=120)  # Field name made lowercase.
    fechainicial_curso = models.DateTimeField(db_column='fechainicial_curso')  # Field name made lowercase.
    fechafinal_curso = models.DateTimeField(db_column='fechafina_curso')  # Field name made lowercase.
    link_curso = models.CharField(db_column='link_curso', max_length=200)  # Field name made lowercase.
    descripcion_curso = models.CharField(db_column='descripcion_curso', max_length=450)  # Field name made lowercase.
    creador = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'cursos'