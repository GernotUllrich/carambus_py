from .branch_cc import BranchCc
from django.db import models

class ChampionshipTypeCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    shortname = models.CharField(max_length=255, blank=True, null=True)
    context = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    branch_cc = models.ForeignKey(BranchCc, on_delete=models.CASCADE,
                                  related_name='championship_type_ccs_for_branch_cc')

    class Meta:
        managed = True
        db_table = 'championship_type_ccs'