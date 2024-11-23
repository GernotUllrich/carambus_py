from django.db import models



class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(blank=True, null=True)
    code = models.CharField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    # regions = rails_models.RelatedField('Regions', related_name='country')

    class Meta:
        managed = False
        db_table = 'countries'