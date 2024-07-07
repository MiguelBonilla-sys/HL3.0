from django.db import models


class AuditLog(models.Model):
    timestamp = models.DateTimeField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    table_name = models.CharField(max_length=255)
    change_type = models.CharField(max_length=6)
    affected_record_id = models.IntegerField(blank=True, null=True)
    modified_data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.user.username  # Asumiendo que AuthUser tiene un campo 'username'
    
    class Meta:
        managed = False
        db_table = 'audit_log'