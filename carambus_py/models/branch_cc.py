from .discipline import Discipline
from .region_cc import RegionCc
from django.db import models

class BranchCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    context = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    # competition_ccs = rails_models.RelatedField('CompetitionCcs', related_name='branchcc')
    # game_plan_ccs = rails_models.RelatedField('GamePlanCcs', related_name='branchcc')
    # group_ccs = rails_models.RelatedField('GroupCcs', related_name='branchcc')
    # registration_list_ccs = rails_models.RelatedField('RegistrationListCcs', related_name='branchcc')
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='branch_ccs_for_discipline')
    # discipline_ccs = rails_models.RelatedField('DisciplineCcs', related_name='branchcc')
    region_cc = models.ForeignKey(RegionCc, on_delete=models.CASCADE, related_name='branch_ccs_for_region_cc')

    # category_ccs = rails_models.RelatedField('CategoryCcs', related_name='branchcc')
    # championship_type_ccs = rails_models.RelatedField('ChampionshipTypeCcs', related_name='branchcc')

    class Meta:
        managed = True
        db_table = 'branch_ccs'
        unique_together = (('region_cc_id', 'cc_id', 'context'),)
        if 'test' in sys.argv:
            managed = False
            unique_together = None