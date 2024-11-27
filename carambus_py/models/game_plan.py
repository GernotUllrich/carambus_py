from django.db import models

class GamePlan(models.Model):
    id = models.BigAutoField(primary_key=True)
    footprint = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    # leagues = rails_models.RelatedField('Leagues', related_name='gameplan')

    class Meta:
        managed = True
        db_table = 'game_plans'