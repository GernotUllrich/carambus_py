from django.db import models


class TableKind(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(blank=True, null=True)
    short = models.CharField(blank=True, null=True)
    measures = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    # disciplines = rails_models.RelatedField('Disciplines', related_name='tablekind')
    # tables = rails_models.RelatedField('Tables', related_name='tablekind')

    class Meta:
        managed = False
        db_table = 'table_kinds'