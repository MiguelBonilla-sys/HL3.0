from django.db import models
from blog.Models.HistorialCambiosModel import HistorialCambios


class Noticias(models.Model):
    idnoticia = models.IntegerField(db_column='idNoticia', primary_key=True)  # Field name made lowercase.
    nombre_noticia = models.CharField(db_column='Nombre_noticia', max_length=600)  # Field name made lowercase.
    fecha_noticia = models.DateTimeField(db_column='Fecha_noticia')  # Field name made lowercase.
    link_noticia = models.CharField(db_column='Link_noticia', max_length=250)  # Field name made lowercase.
    description_noticia = models.CharField(db_column='Description_noticia', max_length=450)  # Field name made lowercase.
    historial_cambios_idhistorial_cambios = models.ForeignKey(HistorialCambios, models.DO_NOTHING, db_column='historial_cambios_idhistorial_cambios', blank=True, null=True)

    class Meta:
        managed = False  # Django no manejará la creación y eliminación de esta tabla
        db_table = 'noticias'