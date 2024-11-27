from .tournament import Tournament
from django.db import models

class TournamentLocal(models.Model):
    id = models.BigAutoField(primary_key=True)
    timeout = models.IntegerField(blank=True, null=True)
    timeouts = models.IntegerField(blank=True, null=True)
    admin_controlled = models.BooleanField(blank=True, null=True)
    gd_has_prio = models.BooleanField(blank=True, null=True)
    sets_to_win = models.IntegerField()
    sets_to_play = models.IntegerField()
    team_size = models.IntegerField()
    fixed_display_left = models.CharField(max_length=255, blank=True, null=True)
    color_remains_with_set = models.BooleanField()
    allow_follow_up = models.BooleanField()
    kickoff_switches_with = models.CharField(max_length=255, blank=True, null=True)
    innings_goal = models.IntegerField(blank=True, null=True)
    balls_goal = models.IntegerField(blank=True, null=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE,
                                   related_name='tournament_local_for_tournament')

    class Meta:
        managed = True
        db_table = 'tournament_locals'