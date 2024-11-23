from django.db import models


class DebugInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    info = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'debug_infos'