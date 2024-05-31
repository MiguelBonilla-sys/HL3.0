# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Cursos(models.Model):
    idcursos = models.AutoField(db_column='idCursos', primary_key=True)  # Field name made lowercase.
    nombre_curso = models.CharField(db_column='Nombre_Curso', max_length=120)  # Field name made lowercase.
    fechainicial_curso = models.DateTimeField(db_column='FechaInicial_Curso')  # Field name made lowercase.
    fechafina_cursol = models.DateTimeField(db_column='FechaFina_Cursol')  # Field name made lowercase.
    link_curso = models.CharField(db_column='Link_Curso', max_length=200)  # Field name made lowercase.
    descripcion_cursol = models.CharField(db_column='Descripcion_Cursol', max_length=450)  # Field name made lowercase.
    historial_cambios_idhistorial_cambios = models.ForeignKey('HistorialCambios', models.DO_NOTHING, db_column='historial_cambios_idhistorial_cambios', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cursos'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HistorialCambios(models.Model):
    idhistorial_cambios = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='IdUsuario')  # Field name made lowercase.
    tabla_afectada = models.CharField(max_length=50)
    id_registro_afectado = models.IntegerField()
    campo_modificado = models.CharField(max_length=100)
    valor_anterior = models.TextField(blank=True, null=True)
    valor_nuevo = models.TextField(blank=True, null=True)
    fecha_hora_cambio = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'historial_cambios'


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


class Noticias(models.Model):
    idnoticia = models.AutoField(db_column='idNoticia', primary_key=True)  # Field name made lowercase.
    nombre_noticia = models.CharField(db_column='Nombre_noticia', max_length=600)  # Field name made lowercase.
    fecha_noticia = models.DateTimeField(db_column='Fecha_noticia')  # Field name made lowercase.
    link_noticia = models.CharField(db_column='Link_noticia', max_length=250)  # Field name made lowercase.
    description_noticia = models.CharField(db_column='Description_noticia', max_length=450)  # Field name made lowercase.
    historial_cambios_idhistorial_cambios = models.ForeignKey(HistorialCambios, models.DO_NOTHING, db_column='historial_cambios_idhistorial_cambios', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'noticias'


class Proyectos(models.Model):
    idproyectos = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(db_column='Nombre_Proyecto', max_length=150)  # Field name made lowercase.
    intengrantes_proyecto = models.CharField(db_column='Intengrantes_Proyecto', max_length=450)  # Field name made lowercase.
    fecha_proyecto = models.DateTimeField(db_column='Fecha_Proyecto')  # Field name made lowercase.
    link_proyecto = models.CharField(db_column='Link_Proyecto', max_length=250)  # Field name made lowercase.
    description_proyecto = models.CharField(db_column='Description_Proyecto', max_length=450)  # Field name made lowercase.
    historial_cambios_idhistorial_cambios = models.ForeignKey(HistorialCambios, models.DO_NOTHING, db_column='historial_cambios_idhistorial_cambios', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyectos'


class TipoUsuario(models.Model):
    idtipo_usuario = models.AutoField(db_column='idTipo_usuario', primary_key=True)  # Field name made lowercase.
    tipo_usuario = models.CharField(db_column='Tipo_usuario', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=45)  # Field name made lowercase.
    contrase├▒a = models.CharField(db_column='Contrase├▒a', unique=True, max_length=45)  # Field name made lowercase.
    idtipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='idTipo_usuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
        unique_together = (('idusuario', 'idtipo_usuario'),)
