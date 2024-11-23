from django.db import models


class Version(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_type = models.CharField(blank=True, null=True)
    item_id = models.BigIntegerField(blank=True, null=True)
    event = models.CharField(blank=True, null=True)
    whodunnit = models.CharField(blank=True, null=True)
    object = models.TextField(blank=True, null=True)
    object_changes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'versions'