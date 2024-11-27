from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

class Seeding(models.Model):
    id = models.BigAutoField(primary_key=True)
    ba_state = models.CharField(max_length=255, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    balls_goal = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    rank = models.IntegerField(blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)

    player = models.ForeignKey('carambus_py.Player', on_delete=models.CASCADE, related_name='seedings_for_player')
    playing_discipline = models.ForeignKey('carambus_py.Discipline', on_delete=models.CASCADE,
                                           related_name='seedings_for_discipline')
    league_team = models.ForeignKey('carambus_py.LeagueTeam', on_delete=models.CASCADE, related_name='seedings_for_league_team')

    tournament_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Polymorphic type
    tournament_id = models.PositiveIntegerField()  # Polymorphic object ID
    tournament = GenericForeignKey('tournament_type', 'tournament_id')  # Combined polymorphic field

    class Meta:
        managed = True
        ordering = ['position']  # Order by position ascending
        db_table = 'seedings'