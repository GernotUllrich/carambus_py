from django.db import models


class Season(models.Model):
    id = models.BigAutoField(primary_key=True)
    ba_id = models.IntegerField(unique=True, blank=True, null=True)
    name = models.CharField(unique=True, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    # tournaments = rails_models.RelatedField('Tournaments', related_name='season')
    # season_participations = rails_models.RelatedField('SeasonParticipations', related_name='season')
    # player_rankings = rails_models.RelatedField('PlayerRankings', related_name='season')
    # season_ccs = rails_models.RelatedField('SeasonCcs', related_name='season')
    # leagues = rails_models.RelatedField('Leagues', related_name='season')

    class Meta:
        managed = False
        db_table = 'seasons'