from django.db import models

class DisciplineTournamentPlan(models.Model):
    id = models.BigAutoField(primary_key=True)
    points = models.IntegerField(blank=True, null=True)
    innings = models.IntegerField(blank=True, null=True)
    players = models.IntegerField(blank=True, null=True)
    player_class = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    tournament_plan = models.ForeignKey('carambus_py.TournamentPlan', on_delete=models.CASCADE,
                                        related_name='discipline_tournament_plans_for_tournament_plan')
    discipline = models.ForeignKey('carambus_py.Discipline', on_delete=models.CASCADE,
                                   related_name='discipline_tournament_plans_for_discipline')

    class Meta:
        managed = True
        db_table = 'discipline_tournament_plans'