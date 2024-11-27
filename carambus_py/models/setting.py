from django.db import models

class Setting(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    region = models.ForeignKey('carambus_py.Region', on_delete=models.CASCADE, related_name='settings_for_region')
    club = models.ForeignKey('carambus_py.Club', on_delete=models.CASCADE, related_name='settings_for_club')
    tournament = models.ForeignKey('carambus_py.Tournament', on_delete=models.CASCADE, related_name='settings_for_tournament')

    class Meta:
        managed = True
        db_table = 'settings'