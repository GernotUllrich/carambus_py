from django.db import models




class LeagueTeam(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(blank=True, null=True)
    shortname = models.CharField(blank=True, null=True)
    ba_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    source_url = models.CharField(blank=True, null=True)
    sync_date = models.DateTimeField(blank=True, null=True)
    cc_id = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    league = models.ForeignKey('League', on_delete=models.CASCADE, related_name='league_teams_for_league')
    club = models.ForeignKey('Club', on_delete=models.CASCADE, related_name='league_teams_for_club')
    # parties_a = rails_models.RelatedField('PartiesA', related_name='leagueteam')
    # parties_b = rails_models.RelatedField('PartiesB', related_name='leagueteam')
    # parties_as_host = rails_models.RelatedField('PartiesAsHost', related_name='leagueteam')
    # no_show_parties = rails_models.RelatedField('NoShowParties', related_name='leagueteam')
    league_team_cc = models.OneToOneField('LeagueTeamCc', on_delete=models.CASCADE, related_name='league_team_for_league_team_cc')
    # seedings = rails_models.RelatedField('Seedings', related_name='leagueteam')

    class Meta:
        managed = False
        db_table = 'league_teams'