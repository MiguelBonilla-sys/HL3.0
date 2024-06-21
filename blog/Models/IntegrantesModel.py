from django.db import models
from django.contrib.auth.models import User

class Integrantes(models.Model):
    idintegrantes = models.AutoField(primary_key=True)
    nombre_integrante = models.CharField(max_length=120)
    semestre = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    link_git = models.CharField(max_length=200)
    imagen = models.TextField()
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.BooleanField()  # Asumiendo que por defecto, un integrante está activo
    class Meta:
        managed = False
        db_table = 'integrantes'