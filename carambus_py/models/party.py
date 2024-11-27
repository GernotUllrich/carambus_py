from .league import League
from .league_team import LeagueTeam
from .location import Location
from .party_cc import PartyCc
from .party_monitor import PartyMonitor
from django.db import models

class Party(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    ba_id = models.IntegerField(blank=True, null=True)
    day_seqno = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    section = models.CharField(max_length=255, blank=True, null=True)
    cc_id = models.IntegerField(blank=True, null=True)
    register_at = models.DateField(blank=True, null=True)
    group = models.CharField(max_length=255, blank=True, null=True)
    round = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    source_url = models.CharField(max_length=255, blank=True, null=True)
    sync_date = models.DateTimeField(blank=True, null=True)
    reported_at = models.DateTimeField(blank=True, null=True)
    reported_by_player_id = models.IntegerField(blank=True, null=True)
    reported_by = models.CharField(max_length=255, blank=True, null=True)
    party_no = models.IntegerField(blank=True, null=True)
    manual_assignment = models.BooleanField(blank=True, null=True)
    continuous_placements = models.BooleanField()
    timeout = models.IntegerField()
    timeouts = models.IntegerField(blank=True, null=True)
    time_out_stoke_preparation_sec = models.IntegerField(blank=True, null=True)
    time_out_warm_up_first_min = models.IntegerField(blank=True, null=True)
    time_out_warm_up_follow_up_min = models.IntegerField(blank=True, null=True)
    sets_to_play = models.IntegerField()
    sets_to_win = models.IntegerField()
    team_size = models.IntegerField()
    fixed_display_left = models.CharField(max_length=255, blank=True, null=True)
    allow_follow_up = models.BooleanField()
    color_remains_with_set = models.BooleanField()
    kickoff_switches_with = models.CharField(max_length=255, blank=True, null=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='parties_for_league')
    # games = rails_models.RelatedField('Games', related_name='party')
    league_team_a = models.ForeignKey(LeagueTeam, on_delete=models.CASCADE, related_name='parties_for_league_team_a')
    league_team_b = models.ForeignKey(LeagueTeam, on_delete=models.CASCADE,
                                      related_name='parties_for_league_for_league_team_b')
    host_league_team = models.ForeignKey(LeagueTeam, on_delete=models.CASCADE,
                                         related_name='parties_for_host_league_team')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='parties_for_location')
    no_show_team = models.ForeignKey(LeagueTeam, on_delete=models.CASCADE, related_name='parties_for_no_show_team')
    party_monitor = models.OneToOneField(PartyMonitor, on_delete=models.CASCADE,
                                         related_name='party_for_party_monitor')
    party_cc = models.OneToOneField(PartyCc, on_delete=models.CASCADE, related_name='party_for_party_cc')

    # party_games = rails_models.RelatedField('PartyGames', related_name='party')
    # seedings = rails_models.RelatedField('Seedings', related_name='party')

    class Meta:
        managed = True
        db_table = 'parties'