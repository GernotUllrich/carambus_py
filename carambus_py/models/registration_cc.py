from django.db import models


class RegistrationCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='registration_ccs_for_player')
    registration_list_cc = models.ForeignKey('RegistrationListCc', on_delete=models.CASCADE, related_name='registration_ccs_for_registration_list_cc')

    class Meta:
        managed = False
        db_table = 'registration_ccs'
        unique_together = (('player_id', 'registration_list_cc_id'),)