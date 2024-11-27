from .discipline import Discipline
from .league import League
from .location import Location
from .region import Region
from .season import Season
from .setting import Setting
from .tournament_cc import TournamentCc
from .tournament_local import TournamentLocal
from .tournament_monitor import TournamentMonitor
from .tournament_plan import TournamentPlan
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models

class Tournament(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    modus = models.CharField(max_length=255, blank=True, null=True)
    age_restriction = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    accredation_end = models.DateTimeField(blank=True, null=True)
    location_text = models.TextField(blank=True, null=True)
    ba_id = models.IntegerField(unique=True, blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    plan_or_show = models.CharField(max_length=255, blank=True, null=True)
    single_or_league = models.CharField(max_length=255, blank=True, null=True)
    shortname = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    ba_state = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    sync_date = models.DateTimeField(blank=True, null=True)
    player_class = models.CharField(max_length=255, blank=True, null=True)
    innings_goal = models.IntegerField(blank=True, null=True)
    balls_goal = models.IntegerField(blank=True, null=True)
    handicap_tournier = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    timeout = models.IntegerField(blank=True, null=True)
    time_out_warm_up_first_min = models.IntegerField(blank=True, null=True)
    time_out_warm_up_follow_up_min = models.IntegerField(blank=True, null=True)
    organizer_id = models.IntegerField(blank=True, null=True)
    organizer_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Polymorphic type
    timeouts = models.IntegerField()
    admin_controlled = models.BooleanField()
    gd_has_prio = models.BooleanField()
    sets_to_win = models.IntegerField()
    sets_to_play = models.IntegerField()
    team_size = models.IntegerField()
    fixed_display_left = models.CharField(max_length=255, blank=True, null=True)
    color_remains_with_set = models.BooleanField()
    allow_follow_up = models.BooleanField()
    continuous_placements = models.BooleanField()
    manual_assignment = models.BooleanField(blank=True, null=True)
    kickoff_switches_with = models.CharField(max_length=255, blank=True, null=True)
    source_url = models.CharField(max_length=255, blank=True, null=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='tournaments_for_discipline')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='tournaments_for_region')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='tournaments_for_season')
    tournament_plan = models.ForeignKey(TournamentPlan, on_delete=models.CASCADE,
                                        related_name='tournaments_for_tournament_plan')
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='tournaments_for_league')
    # seedings = rails_models.RelatedField('Seedings', related_name='tournament')
    # games = rails_models.RelatedField('Games', related_name='tournament')
    # teams = rails_models.RelatedField('Teams', related_name='tournament')
    tournament_monitor = models.OneToOneField(TournamentMonitor, on_delete=models.CASCADE,
                                              related_name='tournament_for_tournament_monitor')
    tournament_cc = models.OneToOneField(TournamentCc, on_delete=models.CASCADE,
                                         related_name='tournament_for_tournament_cc')
    setting = models.OneToOneField(Setting, on_delete=models.CASCADE, related_name='tournaments_for_setting')
    organizer = GenericForeignKey('organizer_type', 'organizer_id')  # Combined polymorphic field
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='tournaments_for_location')
    tournament_local = models.OneToOneField(TournamentLocal, on_delete=models.CASCADE,
                                            related_name='tournament_for_tournament_local')

    class Meta:
        managed = True
        db_table = 'tournaments'