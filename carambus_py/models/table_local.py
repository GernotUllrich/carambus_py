from django.db import models


class TableLocal(models.Model):
    id = models.BigAutoField(primary_key=True)
    tpl_ip_address = models.CharField(blank=True, null=True)
    ip_address = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    event_id = models.CharField(blank=True, null=True)
    event_summary = models.CharField(blank=True, null=True)
    event_creator = models.CharField(blank=True, null=True)
    event_start = models.DateTimeField(blank=True, null=True)
    event_end = models.DateTimeField(blank=True, null=True)
    heater_on_reason = models.CharField(blank=True, null=True)
    heater_off_reason = models.CharField(blank=True, null=True)
    heater_switched_on_at = models.DateTimeField(blank=True, null=True)
    heater_switched_off_at = models.DateTimeField(blank=True, null=True)
    heater = models.BooleanField(blank=True, null=True)
    manual_heater_on_at = models.DateTimeField(blank=True, null=True)
    manual_heater_off_at = models.DateTimeField(blank=True, null=True)
    scoreboard = models.BooleanField(blank=True, null=True)
    scoreboard_on_at = models.DateTimeField(blank=True, null=True)
    scoreboard_off_at = models.DateTimeField(blank=True, null=True)
    table = models.ForeignKey('Table', on_delete=models.CASCADE, related_name='table_local_for_table')

    class Meta:
        managed = False
        db_table = 'table_locals'