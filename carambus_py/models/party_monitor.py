from .party import Party
from django.db import models

class PartyMonitor(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
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
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='party_monitor_for_party')

    # table_monitors = rails_models.RelatedField('TableMonitors', related_name='partymonitor')

    class Meta:
        managed = True
        db_table = 'party_monitors'