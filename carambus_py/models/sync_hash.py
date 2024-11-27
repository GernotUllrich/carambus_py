from django.db import models

class SyncHash(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    md5 = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    doc = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sync_hashes'