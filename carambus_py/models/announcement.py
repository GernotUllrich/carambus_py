from django.db import models


class Announcement(models.Model):
    id = models.BigAutoField(primary_key=True)
    kind = models.CharField(blank=True, null=True)
    title = models.CharField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'announcements'