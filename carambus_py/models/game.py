from .table_monitor import TableMonitor
from .tournament import Tournament
from django.db import models

class Game(models.Model):
    id = models.BigAutoField(primary_key=True)
    roles = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    seqno = models.IntegerField(blank=True, null=True)
    gname = models.CharField(max_length=255, blank=True, null=True)
    group_no = models.IntegerField(blank=True, null=True)
    table_no = models.IntegerField(blank=True, null=True)
    round_no = models.IntegerField(blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    tournament_type = models.CharField(max_length=255, blank=True, null=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='games_for_tournament')
    # game_participations = rails_models.RelatedField('GameParticipations', related_name='game')
    table_monitor = models.OneToOneField(TableMonitor, on_delete=models.CASCADE,
                                         related_name='game_for_table_monitor')
    was_table_monitor = models.OneToOneField(TableMonitor, on_delete=models.CASCADE,
                                             related_name='game_for_was_tournament')

    class Meta:
        managed = True
        db_table = 'games'