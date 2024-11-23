from django.db import models


class PartyGameCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    seqno = models.IntegerField(blank=True, null=True)
    player_a_id = models.IntegerField(blank=True, null=True)
    player_b_id = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    discipline_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    party_cc = models.ForeignKey('PartyCc', on_delete=models.CASCADE, related_name='party_game_ccs_for_party_cc')
    party_game = models.ForeignKey('PartyGame', on_delete=models.CASCADE, related_name='party_game_cc_for_party_game')

    class Meta:
        managed = False
        db_table = 'party_game_ccs'