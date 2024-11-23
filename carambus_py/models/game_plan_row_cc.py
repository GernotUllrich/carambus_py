from django.db import models


class GamePlanRowCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    game_plan_id = models.IntegerField(blank=True, null=True)
    home_brett = models.IntegerField(blank=True, null=True)
    visitor_brett = models.IntegerField(blank=True, null=True)
    sets = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    ppg = models.IntegerField(blank=True, null=True)
    ppu = models.IntegerField(blank=True, null=True)
    ppv = models.IntegerField(blank=True, null=True)
    mpg = models.IntegerField(blank=True, null=True)
    pmv = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, related_name='game_plan_row_ccs_for_discipline')

    class Meta:
        managed = False
        db_table = 'game_plan_row_ccs'