from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class League(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(blank=True, null=True)
    registration_until = models.DateField(blank=True, null=True)
    organizer_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Polymorphic type
    organizer_id = models.IntegerField(blank=True, null=True)
    ba_id = models.IntegerField(blank=True, null=True)
    ba_id2 = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    staffel_text = models.CharField(blank=True, null=True)
    cc_id = models.IntegerField(blank=True, null=True)
    shortname = models.CharField(blank=True, null=True)
    type = models.CharField(blank=True, null=True)
    source_url = models.CharField(blank=True, null=True)
    sync_date = models.DateTimeField(blank=True, null=True)
    cc_id2 = models.IntegerField(blank=True, null=True)
    game_parameters = models.TextField(blank=True, null=True)
    game_plan_locked = models.BooleanField()
    # league_teams = rails_models.RelatedField('LeagueTeams', related_name='league')
    # parties = rails_models.RelatedField('Parties', related_name='league')
    # tournaments = rails_models.RelatedField('Tournaments', related_name='league')
    tournament = GenericForeignKey('organizer_type', 'organizer_id')  # Combined polymorphic field
    game_plan = models.ForeignKey('GamePlan', on_delete=models.CASCADE, related_name='leagues_for_game_plan')
    region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name='leagues_for_region')
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, related_name='leagues_for_discipline')
    season = models.ForeignKey('Season', on_delete=models.CASCADE, related_name='leagues_for_season')
    league_cc = models.OneToOneField('LeagueCc', on_delete=models.CASCADE, related_name='league_for_league_cc')

    class Meta:
        managed = False
        db_table = 'leagues'
        unique_together = (('ba_id', 'ba_id2'),)