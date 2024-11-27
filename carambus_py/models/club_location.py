from django.db import models

class ClubLocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    club = models.ForeignKey('carambus_py.Club', on_delete=models.CASCADE, related_name='club_locations_for_club')
    location = models.ForeignKey('carambus_py.Location', on_delete=models.CASCADE, related_name='club_locations_for_location')

    class Meta:
        managed = True
        db_table = 'club_locations'