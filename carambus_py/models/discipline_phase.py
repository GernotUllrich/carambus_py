from django.db import models

class DisciplinePhase(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    discipline_id = models.IntegerField(blank=True, null=True)
    parent_discipline_id = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'discipline_phases'