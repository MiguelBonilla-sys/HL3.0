from django.db import models
from django.contrib.auth.models import User

class HistorialCambios(models.Model):
    idhistorial_cambios = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey(User, models.DO_NOTHING)  # Field name made lowercase.
    tabla_afectada = models.CharField(max_length=50)
    id_registro_afectado = models.IntegerField()
    campo_modificado = models.CharField(max_length=100)
    valor_anterior = models.TextField(blank=True, null=True)
    valor_nuevo = models.TextField(blank=True, null=True)
    fecha_hora_cambio = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'historial_cambios'