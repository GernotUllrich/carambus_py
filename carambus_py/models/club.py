from django.db import models




class Club(models.Model):
    id = models.BigAutoField(primary_key=True)
    ba_id = models.IntegerField(unique=True, blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    shortname = models.CharField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    homepage = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    priceinfo = models.TextField(blank=True, null=True)
    logo = models.CharField(blank=True, null=True)
    status = models.CharField(blank=True, null=True)
    founded = models.CharField(blank=True, null=True)
    dbu_entry = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    cc_id = models.IntegerField(blank=True, null=True)
    dbu_nr = models.IntegerField(blank=True, null=True)
    synonyms = models.TextField(blank=True, null=True)
    source_url = models.CharField(blank=True, null=True)
    sync_date = models.DateTimeField(blank=True, null=True)
    region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name='clubs_for_region')
    # players = rails_models.RelatedField('Players', related_name='club')
    # season_participations = rails_models.RelatedField('SeasonParticipations', related_name='club')
    # players = rails_models.RelatedField('Players', related_name='club')
    # club_locations = rails_models.RelatedField('ClubLocations', related_name='club')
    # locations = rails_models.RelatedField('Locations', related_name='club')
    # organized_tournaments = rails_models.RelatedField('OrganizedTournaments', related_name='club')
    # league_teams = rails_models.RelatedField('LeagueTeams', related_name='club')

    class Meta:
        managed = False
        db_table = 'clubs'