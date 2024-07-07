from django.db import models
from django.contrib.auth.models import User

class Noticias(models.Model):
    idnoticia = models.AutoField(db_column='idnoticia', primary_key=True)  # Field name made lowercase.
    nombre_noticia = models.CharField(db_column='nombre_noticia', max_length=600)  # Field name made lowercase.
    fecha_noticia = models.DateTimeField(db_column='fecha_noticia')  # Field name made lowercase.
    link_noticia = models.CharField(db_column='link_noticia', max_length=250)  # Field name made lowercase.
    description_noticia = models.CharField(db_column='description_noticia', max_length=450)  # Field name made lowercase.
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    fuente = models.CharField(max_length=250, blank=True, null=True)
    imagen_noticia = models.TextField()
    class Meta:
        managed = False
        db_table = 'noticias'
