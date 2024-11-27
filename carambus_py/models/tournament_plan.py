from django.db import models

class TournamentPlan(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    rulesystem = models.TextField(blank=True, null=True)
    players = models.IntegerField(blank=True, null=True)
    tables = models.IntegerField(blank=True, null=True)
    more_description = models.TextField(blank=True, null=True)
    even_more_description = models.TextField(blank=True, null=True)
    executor_class = models.CharField(max_length=255, blank=True, null=True)
    executor_params = models.TextField(blank=True, null=True)
    ngroups = models.IntegerField(blank=True, null=True)
    nrepeats = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    # discipline_tournament_plans = rails_models.RelatedField('DisciplineTournamentPlans', related_name='tournamentplan')
    # tournaments = rails_models.RelatedField('Tournaments', related_name='tournamentplan')

    class Meta:
        managed = True
        db_table = 'tournament_plans'