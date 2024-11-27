from django.db import models

class LeagueCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    context = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    shortname = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    report_form = models.CharField(max_length=255, blank=True, null=True)
    report_form_data = models.CharField(max_length=255, blank=True, null=True)
    cc_id2 = models.IntegerField(blank=True, null=True)
    season_cc = models.ForeignKey('carambus_py.SeasonCc', on_delete=models.CASCADE, related_name='league_ccs_for_season_cc')
    league = models.ForeignKey('carambus_py.League', on_delete=models.CASCADE, related_name='league_ccs_for_league')
    game_plan_cc = models.ForeignKey('carambus_py.GamePlanCc', on_delete=models.CASCADE, related_name='league_ccs_for_game_plan_cc')

    # league_team_ccs = rails_models.RelatedField('LeagueTeamCcs', related_name='leaguecc')
    # party_ccs = rails_models.RelatedField('PartyCcs', related_name='leaguecc')

    class Meta:
        managed = True
        db_table = 'league_ccs'