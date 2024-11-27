from .discipline import Discipline
from .player import Player
from .player_class import PlayerClass
from .region import Region
from .season import Season
from django.db import models

class PlayerRanking(models.Model):
    id = models.BigAutoField(primary_key=True)
    org_level = models.CharField(max_length=255, blank=True, null=True)
    innings = models.IntegerField(blank=True, null=True)
    tournament_player_class_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    gd = models.FloatField(blank=True, null=True)
    hs = models.IntegerField(blank=True, null=True)
    bed = models.FloatField(blank=True, null=True)
    btg = models.FloatField(blank=True, null=True)
    p_gd = models.FloatField(blank=True, null=True)
    pp_gd = models.FloatField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    g = models.IntegerField(blank=True, null=True)
    v = models.IntegerField(blank=True, null=True)
    quote = models.FloatField(blank=True, null=True)
    sp_g = models.IntegerField(blank=True, null=True)
    sp_v = models.IntegerField(blank=True, null=True)
    sp_quote = models.FloatField(blank=True, null=True)
    balls = models.IntegerField(blank=True, null=True)
    sets = models.IntegerField(blank=True, null=True)
    t_ids = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE,
                                   related_name='player_rankings_for_discipline')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_rankings_for_player')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='player_rankings_for_region')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='player_rankings_for_season')
    player_class = models.ForeignKey(PlayerClass, on_delete=models.CASCADE,
                                     related_name='player_rankings_for_player_class')
    p_player_class = models.ForeignKey(PlayerClass, on_delete=models.CASCADE,
                                       related_name='player_rankings_for_p_player_class')
    pp_player_class = models.ForeignKey(PlayerClass, on_delete=models.CASCADE,
                                        related_name='player_rankings_for_pp_player_class')

    class Meta:
        managed = True
        db_table = 'player_rankings'