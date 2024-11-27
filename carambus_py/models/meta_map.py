from django.db import models

class MetaMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    class_ba = models.CharField(max_length=255, blank=True, null=True)
    class_cc = models.CharField(max_length=255, blank=True, null=True)
    ba_base_url = models.CharField(max_length=255, blank=True, null=True)
    cc_base_url = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'meta_maps'  # your_project/tests/utils/models_import_helper.py