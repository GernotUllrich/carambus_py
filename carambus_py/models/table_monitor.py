from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class TableMonitor(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    next_game_id = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    ip_address = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    active_timer = models.CharField(blank=True, null=True)
    timer_start_at = models.DateTimeField(blank=True, null=True)
    timer_finish_at = models.DateTimeField(blank=True, null=True)
    timer_halt_at = models.DateTimeField(blank=True, null=True)
    nnn = models.IntegerField(blank=True, null=True)
    panel_state = models.CharField()
    current_element = models.CharField()
    timer_job_id = models.CharField(blank=True, null=True)
    clock_job_id = models.CharField(blank=True, null=True)
    copy_from = models.IntegerField(blank=True, null=True)
    tournament_monitor_type = models.CharField(blank=True, null=True)
    prev_data = models.TextField(blank=True, null=True)
    prev_tournament_monitor_id = models.IntegerField(blank=True, null=True)
    prev_tournament_monitor_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Polymorphic type
    tournament_monitor = models.ForeignKey('TournamentMonitor', on_delete=models.CASCADE, related_name='table_monitors_for_tournament_monitor')
    game = models.ForeignKey('Game', on_delete=models.SET_NULL, null=True, related_name='table_monitor_for_game')
    prev_game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='table_monitors_for_prev_game')
    prev_tournament_monitor = GenericForeignKey('prev_tournament_monitor_type', 'prev_tournament_monitor_id')  # Combined polymorphic field
    table = models.OneToOneField('Table', on_delete=models.CASCADE, related_name='table_monitors_for_table')

    class Meta:
        managed = False
        db_table = 'table_monitors'