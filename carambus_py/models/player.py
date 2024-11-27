from django.db import models

class Player(models.Model):
    id = models.BigAutoField(primary_key=True)
    ba_id = models.IntegerField(unique=True, blank=True, null=True)
    club_id = models.IntegerField(blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    guest = models.BooleanField()
    nickname = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    tournament_id = models.IntegerField(blank=True, null=True)
    cc_id = models.IntegerField(blank=True, null=True)
    dbu_nr = models.IntegerField(blank=True, null=True)
    dbu_pass_nr = models.IntegerField(blank=True, null=True)
    fl_name = models.CharField(max_length=255, blank=True, null=True)
    source_url = models.CharField(max_length=255, blank=True, null=True)
    sync_date = models.DateTimeField(blank=True, null=True)
    nrw_nr = models.IntegerField(blank=True, null=True)
    pin4 = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)

    # game_participations = rails_models.RelatedField('GameParticipations', related_name='player')
    # season_participations = rails_models.RelatedField('SeasonParticipations', related_name='player')
    # clubs = rails_models.RelatedField('Clubs', related_name='player')
    # player_rankings = rails_models.RelatedField('PlayerRankings', related_name='player')
    # seedings = rails_models.RelatedField('Seedings', related_name='player')
    # registration_ccs = rails_models.RelatedField('RegistrationCcs', related_name='player')
    # party_a_games = rails_models.RelatedField('PartyAGames', related_name='player')
    # party_b_games = rails_models.RelatedField('PartyBGames', related_name='player')
    # admin_user = models.OneToOneField(User', on_delete=models.CASCADE, related_name='player_for_user')

    class Meta:
        managed = True
        db_table = 'players'