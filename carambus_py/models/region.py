from .country import Country
from .region_cc import RegionCc
from .setting import Setting
from django.db import models

class Region(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    shortname = models.CharField(unique=True, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    public_cc_url_base = models.CharField(max_length=255, blank=True, null=True)
    dbu_name = models.CharField(max_length=255, blank=True, null=True)
    telefon = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    opening = models.CharField(max_length=255, blank=True, null=True)
    source_url = models.CharField(max_length=255, blank=True, null=True)
    sync_date = models.DateTimeField(blank=True, null=True)
    cc_id = models.IntegerField(blank=True, null=True)
    scrape_data = models.TextField(blank=True, null=True)

    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='regions_for_country')
    # clubs = rails_models.RelatedField('Clubs', related_name='region')
    # tournaments = rails_models.RelatedField('Tournaments', related_name='region')
    # player_rankings = rails_models.RelatedField('PlayerRankings', related_name='region')
    # locations = rails_models.RelatedField('Locations', related_name='region')
    # organized_tournaments = rails_models.RelatedField('OrganizedTournaments', related_name='region')
    # organized_leagues = rails_models.RelatedField('OrganizedLeagues', related_name='region')
    setting = models.OneToOneField(Setting, on_delete=models.CASCADE, related_name='region_for_setting')
    # leagues = rails_models.RelatedField('Leagues', related_name='region')
    region_cc = models.OneToOneField(RegionCc, on_delete=models.CASCADE, related_name='region_for_region_cc')

    class Meta:
        managed = True
        db_table = 'regions'