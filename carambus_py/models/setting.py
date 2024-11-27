from .club import Club
from .region import Region
from .tournament import Tournament
from django.db import models

class Setting(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='settings_for_region')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='settings_for_club')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='settings_for_tournament')

    class Meta:
        managed = True
        db_table = 'settings'