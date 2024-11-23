from django.db import models


class SyncHash(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(blank=True, null=True)
    md5 = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    doc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sync_hashes'