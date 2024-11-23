from django.db import models


class Upload(models.Model):
    id = models.BigAutoField(primary_key=True)
    filename = models.CharField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'uploads'