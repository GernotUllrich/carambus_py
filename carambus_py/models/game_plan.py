from django.db import models


class GamePlan(models.Model):
    id = models.BigAutoField(primary_key=True)
    footprint = models.CharField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    # leagues = rails_models.RelatedField('Leagues', related_name='gameplan')

    class Meta:
        managed = False
        db_table = 'game_plans'