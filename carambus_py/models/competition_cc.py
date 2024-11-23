from django.db import models


class CompetitionCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    context = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    branch_cc = models.ForeignKey('BranchCc', on_delete=models.CASCADE, related_name='competition_ccs_for_branch_cc')
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, related_name='competition_ccs_for_discipline')
    # season_ccs = rails_models.RelatedField('SeasonCcs', related_name='competitioncc')

    class Meta:
        managed = False
        db_table = 'competition_ccs'
        unique_together = (('branch_cc_id', 'cc_id', 'context'),)
