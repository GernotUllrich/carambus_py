from .game import Game
from .player import Player
from django.db import models
import sys

class GameParticipation(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    result = models.IntegerField(blank=True, null=True)
    innings = models.IntegerField(blank=True, null=True)
    gd = models.FloatField(blank=True, null=True)
    hs = models.IntegerField(blank=True, null=True)
    gname = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sets = models.IntegerField(blank=True, null=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='game_participations_for_player')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game_participations_for_game')

    class Meta:
        managed = True
        db_table = 'game_participations'
        unique_together = (('game_id', 'player_id', 'role'),)
        if 'test' in sys.argv:
            managed = False
            unique_together = None