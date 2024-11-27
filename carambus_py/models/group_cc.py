from django.db import models

class GroupCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    context = models.CharField(max_length=255, blank=True, null=True)
    display = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    branch_cc = models.ForeignKey('carambus_py.BranchCc', on_delete=models.CASCADE, related_name='group_ccs_for_branch_cc')

    # tournament_cc = rails_models.RelatedField('TournamentCc', related_name='groupcc')
    # registration_list_ccs = rails_models.RelatedField('RegistrationListCcs', related_name='groupcc')

    class Meta:
        managed = True
        db_table = 'group_ccs'