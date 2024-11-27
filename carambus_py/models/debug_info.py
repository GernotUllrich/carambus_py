from django.db import models

class DebugInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    info = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'debug_infos'