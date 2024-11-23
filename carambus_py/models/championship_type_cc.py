from django.db import models


class ChampionshipTypeCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    shortname = models.CharField(blank=True, null=True)
    context = models.CharField(blank=True, null=True)
    status = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    branch_cc = models.ForeignKey('BranchCc', on_delete=models.CASCADE, related_name='championship_type_ccs_for_branch_cc')

    class Meta:
        managed = False
        db_table = 'championship_type_ccs'