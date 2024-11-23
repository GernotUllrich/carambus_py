from django.db import models


class Slot(models.Model):
    id = models.BigAutoField(primary_key=True)
    dayofweek = models.IntegerField(blank=True, null=True)
    hourofday_start = models.IntegerField(blank=True, null=True)
    minuteofhour_start = models.IntegerField(blank=True, null=True)
    hourofday_end = models.IntegerField(blank=True, null=True)
    minuteofhour_end = models.IntegerField(blank=True, null=True)
    next_start = models.DateTimeField(blank=True, null=True)
    next_end = models.DateTimeField(blank=True, null=True)
    table_id = models.IntegerField(blank=True, null=True)
    recurring = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'slots'