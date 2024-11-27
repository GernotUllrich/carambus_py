from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.contrib.contenttypes.models import ContentType

class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    organizer_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Polymorphic type
    organizer_id = models.IntegerField(blank=True, null=True)
    md5 = models.CharField(unique=True)
    synonyms = models.TextField(blank=True, null=True)
    source_url = models.CharField(max_length=255, blank=True, null=True)
    sync_date = models.DateTimeField(blank=True, null=True)
    cc_id = models.IntegerField(blank=True, null=True)
    dbu_nr = models.IntegerField(blank=True, null=True)
    club = models.ForeignKey('carambus_py.Club', on_delete=models.CASCADE, related_name='locations_for_club')
    # club_locations = rails_models.RelatedField('ClubLocations', related_name='location')
    # clubs = rails_models.RelatedField('Clubs', related_name='location')
    # parties = rails_models.RelatedField('Parties', related_name='location')
    region = models.ForeignKey('carambus_py.Region', on_delete=models.CASCADE, related_name='locations_for_region')
    organizer = GenericForeignKey('organizer_type', 'organizer_id')  # Combined polymorphic field

    # tables = rails_models.RelatedField('Tables', related_name='location')
    # tournaments = rails_models.RelatedField('Tournaments', related_name='location')

    class Meta:
        managed = True
        db_table = 'locations'