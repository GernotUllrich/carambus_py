from .region import Region
from django.db import models

class RegionCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    context = models.CharField(unique=True, blank=True, null=True)
    shortname = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    base_url = models.CharField(max_length=255, blank=True, null=True)
    public_url = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    userpw = models.CharField(max_length=255, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='region_ccs_for_region')

    # branch_ccs = rails_models.RelatedField('BranchCcs', related_name='regioncc')

    class Meta:
        managed = True
        db_table = 'region_ccs'
        unique_together = (('cc_id', 'context'),)
        if 'test' in sys.argv:
            managed = False
            unique_together = None