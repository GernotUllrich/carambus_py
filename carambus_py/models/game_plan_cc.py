from .branch_cc import BranchCc
from .discipline import Discipline
from django.db import models

class GamePlanCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    mp_won = models.IntegerField(blank=True, null=True)
    mb_draw = models.IntegerField(blank=True, null=True)
    mp_lost = models.IntegerField(blank=True, null=True)
    znp = models.IntegerField(blank=True, null=True)
    vorgabe = models.IntegerField(blank=True, null=True)
    plausi = models.BooleanField(blank=True, null=True)
    pez_partie = models.CharField(max_length=255, blank=True, null=True)
    bez_brett = models.CharField(max_length=255, blank=True, null=True)
    rang_partie = models.IntegerField(blank=True, null=True)
    rang_mgd = models.IntegerField(blank=True, null=True)
    rang_kegel = models.IntegerField(blank=True, null=True)
    ersatzspieler_regel = models.IntegerField(blank=True, null=True)
    row_type_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    branch_cc = models.ForeignKey(BranchCc, on_delete=models.CASCADE, related_name='game_plan_ccs_for_branch_cc')
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='game_plan_ccs_for_discipline')

    # league_ccs = rails_models.RelatedField('LeagueCcs', related_name='gameplancc')

    class Meta:
        managed = True
        db_table = 'game_plan_ccs'