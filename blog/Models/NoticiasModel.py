from django.db import models
from django.contrib.auth.models import User as AuthUser

class Noticias(models.Model):
    idnoticia = models.AutoField(db_column='idNoticia', primary_key=True)  # Field name made lowercase.
    nombre_noticia = models.CharField(db_column='Nombre_noticia', max_length=600)  # Field name made lowercase.
    fecha_noticia = models.DateTimeField(db_column='Fecha_noticia')  # Field name made lowercase.
    link_noticia = models.CharField(db_column='Link_noticia', max_length=250)  # Field name made lowercase.
    description_noticia = models.CharField(db_column='Description_noticia', max_length=450)  # Field name made lowercase.
    creador = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'noticias'
