from django.db import models


class CalendarEvent(models.Model):
    id = models.BigAutoField(primary_key=True)
    summary = models.CharField(blank=True, null=True)
    recurring = models.BooleanField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    event_start = models.DateTimeField(blank=True, null=True)
    event_end = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'calendar_events'