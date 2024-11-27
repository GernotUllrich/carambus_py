from django.db import models
import sys

class SeasonCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    context = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    competition_cc = models.ForeignKey('carambus_py.CompetitionCc', on_delete=models.CASCADE,
                                       related_name='season_cc_for_competition_cc')
    season = models.ForeignKey('carambus_py.Season', on_delete=models.CASCADE, related_name='season_cc_for_season')

    # league_ccs = rails_models.RelatedField('LeagueCcs', related_name='seasoncc')
    # registration_list_ccs = rails_models.RelatedField('RegistrationListCcs', related_name='seasoncc')

    class Meta:
        managed = True
        db_table = 'season_ccs'
        unique_together = (('competition_cc_id', 'cc_id', 'context'),)
        if 'test' in sys.argv:
            managed = False
            unique_together = None