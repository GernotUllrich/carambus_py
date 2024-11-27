from django.db import models

class PartyGame(models.Model):
    id = models.BigAutoField(primary_key=True)
    seqno = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    data = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    party = models.ForeignKey('carambus_py.Party', on_delete=models.CASCADE, related_name='party_games_for_party')
    player_a = models.ForeignKey('carambus_py.Player', on_delete=models.CASCADE, related_name='party_games_for_player_a')
    player_b = models.ForeignKey('carambus_py.Player', on_delete=models.CASCADE, related_name='party_games_for_player_b')
    discipline = models.ForeignKey('carambus_py.Discipline', on_delete=models.CASCADE, related_name='party_games_for_discipline')
    party_game_cc = models.OneToOneField('carambus_py.PartyGameCc', on_delete=models.CASCADE,
                                         related_name='party_game_for_party_game_cc')

    class Meta:
        managed = True
        db_table = 'party_games'