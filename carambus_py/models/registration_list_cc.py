from django.db import models

class RegistrationListCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    context = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    qualifying_date = models.DateTimeField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    branch_cc = models.ForeignKey('carambus_py.BranchCc', on_delete=models.CASCADE,
                                  related_name='registration_list_ccs_for_branch_cc')
    season = models.ForeignKey('carambus_py.Season', on_delete=models.CASCADE, related_name='registration_list_ccs_for_season')
    discipline = models.ForeignKey('carambus_py.Discipline', on_delete=models.CASCADE,
                                   related_name='registration_list_ccs_for_discipline')
    category_cc = models.ForeignKey('carambus_py.CategoryCc', on_delete=models.CASCADE,
                                    related_name='registration_list_ccs_for_category_cc')

    # registration_ccs = rails_models.RelatedField('RegistrationCcs', related_name='registrationlistcc')

    class Meta:
        managed = True
        db_table = 'registration_list_ccs'