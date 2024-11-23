# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange rails_models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the rails_models, but don't rename db_table values or field names.
from django.db import models


class Tournament(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(blank=True, null=True)
    discipline_id = models.IntegerField(blank=True, null=True)
    modus = models.CharField(blank=True, null=True)
    age_restriction = models.CharField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    accredation_end = models.DateTimeField(blank=True, null=True)
    location_text = models.TextField(blank=True, null=True)
    ba_id = models.IntegerField(unique=True, blank=True, null=True)
    season_id = models.IntegerField(blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    plan_or_show = models.CharField(blank=True, null=True)
    single_or_league = models.CharField(blank=True, null=True)
    shortname = models.CharField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    ba_state = models.CharField(blank=True, null=True)
    state = models.CharField(blank=True, null=True)
    sync_date = models.DateTimeField(blank=True, null=True)
    player_class = models.CharField(blank=True, null=True)
    tournament_plan_id = models.IntegerField(blank=True, null=True)
    innings_goal = models.IntegerField(blank=True, null=True)
    balls_goal = models.IntegerField(blank=True, null=True)
    handicap_tournier = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    timeout = models.IntegerField(blank=True, null=True)
    time_out_warm_up_first_min = models.IntegerField(blank=True, null=True)
    time_out_warm_up_follow_up_min = models.IntegerField(blank=True, null=True)
    organizer_id = models.IntegerField(blank=True, null=True)
    organizer_type = models.CharField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    timeouts = models.IntegerField()
    admin_controlled = models.BooleanField()
    gd_has_prio = models.BooleanField()
    league_id = models.IntegerField(blank=True, null=True)
    sets_to_win = models.IntegerField()
    sets_to_play = models.IntegerField()
    team_size = models.IntegerField()
    fixed_display_left = models.CharField(blank=True, null=True)
    color_remains_with_set = models.BooleanField()
    allow_follow_up = models.BooleanField()
    continuous_placements = models.BooleanField()
    manual_assignment = models.BooleanField(blank=True, null=True)
    kickoff_switches_with = models.CharField(blank=True, null=True)
    source_url = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tournaments'
