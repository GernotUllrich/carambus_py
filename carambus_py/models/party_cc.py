from .league_cc import LeagueCc
from .league_team_cc import LeagueTeamCc
from .party import Party
from django.db import models

class PartyCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    day_seqno = models.IntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    register_at = models.DateField(blank=True, null=True)
    group = models.CharField(max_length=255, blank=True, null=True)
    round = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    match_id = models.IntegerField(blank=True, null=True)
    league_cc = models.ForeignKey(LeagueCc, on_delete=models.CASCADE, related_name='party_ccs_for_league_cc')
    league_team_a_cc = models.ForeignKey(LeagueTeamCc, on_delete=models.CASCADE,
                                         related_name='party_ccs_for_league_team_a_cc')
    league_team_b_cc = models.ForeignKey(LeagueTeamCc, on_delete=models.CASCADE,
                                         related_name='party_ccs_for_league_team_b_cc')
    league_team_host_cc = models.ForeignKey(LeagueTeamCc, on_delete=models.CASCADE,
                                            related_name='party_ccs_for_league_team_host_cc')
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='party_cc_for_party')

    # party_game_ccs = rails_models.RelatedField('PartyGameCcs', related_name='partycc')

    class Meta:
        managed = True
        db_table = 'party_ccs'