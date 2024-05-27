from django.db import models

class TipoUsuario(models.Model):
    idtipo_usuario = models.AutoField(db_column='idTipo_usuario', primary_key=True)  # Field name made lowercase.
    tipo_usuario = models.CharField(db_column='Tipo_usuario', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=45)  # Field name made lowercase.
    contraseña = models.CharField(db_column='contraseña', unique=True, max_length=45)  # Field name made lowercase.
    idtipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='idTipo_usuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
        unique_together = (('idusuario', 'idtipo_usuario'),)