from django.db import models


class CategoryCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    context = models.CharField(blank=True, null=True)
    max_age = models.IntegerField(blank=True, null=True)
    min_age = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    sex = models.CharField(blank=True, null=True)
    status = models.CharField(blank=True, null=True)
    cc_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    # registration_list_ccs = rails_models.RelatedField('RegistrationListCcs', related_name='categorycc')
    # tournament_ccs = rails_models.RelatedField('TournamentCcs', related_name='categorycc')
    branch_cc = models.ForeignKey('BranchCc', on_delete=models.CASCADE, related_name='category_ccs_for_branch_cc')

    class Meta:
        managed = False
        db_table = 'category_ccs'