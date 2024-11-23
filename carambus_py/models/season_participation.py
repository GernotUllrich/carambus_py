from django.db import models


class SeasonParticipation(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.CharField(blank=True, null=True)
    ba_id = models.IntegerField(blank=True, null=True)
    source_url = models.CharField(blank=True, null=True)
    sync_date = models.DateTimeField(blank=True, null=True)
    season = models.ForeignKey('Season', on_delete=models.CASCADE, related_name='season_participations_for_season')
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='season_participations_for_player')
    club = models.ForeignKey('Club', on_delete=models.CASCADE, related_name='season_participations_for_club')

    class Meta:
        managed = False
        db_table = 'season_participations'
        unique_together = (('player_id', 'club_id', 'season_id'),)
