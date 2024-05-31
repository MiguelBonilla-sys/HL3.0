from django.db import models
from blog.Models.UsuariosModel import Usuario


class HistorialCambios(models.Model):
    idhistorial_cambios = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='IdUsuario')  # Field name made lowercase.
    tabla_afectada = models.CharField(max_length=50)
    id_registro_afectado = models.IntegerField()
    campo_modificado = models.CharField(max_length=100)
    valor_anterior = models.TextField(blank=True, null=True)
    valor_nuevo = models.TextField(blank=True, null=True)
    fecha_hora_cambio = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'historial_cambios'