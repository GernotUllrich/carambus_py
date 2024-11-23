from django.db import models


class Table(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    ip_address = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    tpl_ip_address = models.IntegerField(blank=True, null=True)
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
    heater_auto = models.BooleanField(blank=True, null=True)
    location = models.ForeignKey('Location', models.DO_NOTHING, blank=True, null=True, related_name='tables_for_location')
    table_kind = models.ForeignKey('TableKind', models.DO_NOTHING, blank=True, null=True, related_name='tables_for_table_kind')
    table_monitor = models.ForeignKey('TableMonitor', on_delete=models.DO_NOTHING, related_name='table_for_table_monitor')
    table_local = models.OneToOneField('TableLocal', on_delete=models.CASCADE, related_name='table_for_table_local')

    class Meta:
        managed = False
        db_table = 'tables'