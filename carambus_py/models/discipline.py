import sys

from django.db import models

class Discipline(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    type = models.CharField(max_length=255, blank=True, null=True)
    synonyms = models.TextField(blank=True, null=True)
    team_size = models.IntegerField(blank=True, null=True)
    table_kind = models.ForeignKey('carambus_py.TableKind', on_delete=models.CASCADE, related_name='disciplines_for_table_kind')
    super_discipline = models.ForeignKey('self', on_delete=models.CASCADE,
                                         related_name='sub_disciplines', blank=True, null=True)
    # sub_disciplines = rails_models.RelatedField('SubDisciplines', related_name='discipline')
    # tournaments = rails_models.RelatedField('Tournaments', related_name='discipline')
    # player_classes = rails_models.RelatedField('PlayerClasses', related_name='discipline')
    # player_rankings = rails_models.RelatedField('PlayerRankings', related_name='discipline')
    discipline_cc = models.OneToOneField('carambus_py.DisciplineCc', on_delete=models.CASCADE,
                                         related_name='discipline_for_discipline_cc')
    # leagues = rails_models.RelatedField('Leagues', related_name='discipline')
    # game_plan_ccs = rails_models.RelatedField('GamePlanCcs', related_name='discipline')
    # game_plan_row_ccs = rails_models.RelatedField('GamePlanRowCcs', related_name='discipline')
    # seeding_plays = rails_models.RelatedField('SeedingPlays', related_name='discipline')
    competition_cc = models.OneToOneField('carambus_py.CompetitionCc', on_delete=models.CASCADE,
                                          related_name='discipline_for_competition_cc')
    branch_cc = models.OneToOneField('carambus_py.BranchCc', on_delete=models.CASCADE, related_name='discipline_for_branch_cc')

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'disciplines'
        unique_together = (('name', 'table_kind_id'), ('name', 'table_kind_id'),)
        if 'test' in sys.argv:
            managed = False
            unique_together = None