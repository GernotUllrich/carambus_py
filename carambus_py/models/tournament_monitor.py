from django.db import models

class TournamentMonitor(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    innings_goal = models.IntegerField(blank=True, null=True)
    balls_goal = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    timeouts = models.IntegerField(blank=True, null=True)
    timeout = models.IntegerField()
    sets_to_win = models.IntegerField()
    sets_to_play = models.IntegerField()
    fixed_display_left = models.CharField(max_length=255, blank=True, null=True)
    color_remains_with_set = models.BooleanField()
    team_size = models.IntegerField()
    allow_follow_up = models.BooleanField()
    allow_overflow = models.BooleanField(blank=True, null=True)
    kickoff_switches_with = models.CharField(max_length=255, blank=True, null=True)
    tournament = models.ForeignKey('carambus_py.Tournament', on_delete=models.CASCADE,
                                   related_name='tournament_monitor_for_tournament')

    # table_monitors = rails_models.RelatedField('TableMonitors', related_name='tournamentmonitor')
    # was_table_monitors = rails_models.RelatedField('WasTableMonitors', related_name='tournamentmonitor')

    class Meta:
        managed = True
        db_table = 'tournament_monitors'