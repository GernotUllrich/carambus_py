from django.db import models


class LeagueTeamCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    shortname = models.CharField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    league_cc = models.ForeignKey('LeagueCc', on_delete=models.CASCADE, related_name='league_team_ccs_for_league_cc')
    league_team = models.ForeignKey('LeagueTeam', on_delete=models.CASCADE, related_name='league_team_ccs_for_league_team')
    # party_a_ccs = rails_models.RelatedField('PartyACcs', related_name='leagueteamcc')
    # party_b_ccs = rails_models.RelatedField('PartyBCcs', related_name='leagueteamcc')
    # party_host_ccs = rails_models.RelatedField('PartyHostCcs', related_name='leagueteamcc')

    class Meta:
        managed = False
        db_table = 'league_team_ccs'