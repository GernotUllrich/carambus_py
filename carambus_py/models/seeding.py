from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Seeding(models.Model):
    id = models.BigAutoField(primary_key=True)
    ba_state = models.CharField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    state = models.CharField(blank=True, null=True)
    balls_goal = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    rank = models.IntegerField(blank=True, null=True)
    role = models.CharField(blank=True, null=True)

    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='seedings_for_player')
    playing_discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, related_name='seedings_for_discipline')
    league_team = models.ForeignKey('LeagueTeam', on_delete=models.CASCADE, related_name='seedings_for_league_team')

    tournament_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Polymorphic type
    tournament_id = models.PositiveIntegerField()  # Polymorphic object ID
    tournament = GenericForeignKey('tournament_type', 'tournament_id')  # Combined polymorphic field

    class Meta:
        managed = False
        ordering = ['position']  # Order by position ascending
        db_table = 'seedings'