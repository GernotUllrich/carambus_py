from django.db import models


class SeasonCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    context = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    competition_cc = models.ForeignKey('CompetitionCc', on_delete=models.CASCADE, related_name='season_cc_for_competition_cc')
    season = models.ForeignKey('Season', on_delete=models.CASCADE, related_name='season_cc_for_season')
    # league_ccs = rails_models.RelatedField('LeagueCcs', related_name='seasoncc')
    # registration_list_ccs = rails_models.RelatedField('RegistrationListCcs', related_name='seasoncc')

    class Meta:
        managed = False
        db_table = 'season_ccs'
        unique_together = (('competition_cc_id', 'cc_id', 'context'),)
