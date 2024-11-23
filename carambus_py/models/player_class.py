from django.db import models


class PlayerClass(models.Model):
    id = models.BigAutoField(primary_key=True)
    shortname = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, related_name='player_classes_for_discipline')
    # player_rankings = rails_models.RelatedField('PlayerRankings', related_name='playerclass')
    # p_player_rankings = rails_models.RelatedField('PPlayerRankings', related_name='playerclass')
    # pp_player_rankings = rails_models.RelatedField('PpPlayerRankings', related_name='playerclass')
    # tournament_player_rankings = rails_models.RelatedField('TournamentPlayerRankings', related_name='playerclass')

    class Meta:
        managed = False
        db_table = 'player_classes'