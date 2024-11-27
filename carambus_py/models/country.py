from django.db import models

class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    # regions = rails_models.RelatedField('Regions', related_name='country')

    class Meta:
        managed = True
        db_table = 'countries'