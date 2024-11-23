from django.db import models

class Discipline(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    type = models.CharField(blank=True, null=True)
    synonyms = models.TextField(blank=True, null=True)
    team_size = models.IntegerField(blank=True, null=True)
    table_kind = models.ForeignKey('TableKind', on_delete=models.CASCADE, related_name='disciplines_for_table_kind')
    super_discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, related_name='disciplines_for_discipline')
    # sub_disciplines = rails_models.RelatedField('SubDisciplines', related_name='discipline')
    # tournaments = rails_models.RelatedField('Tournaments', related_name='discipline')
    # player_classes = rails_models.RelatedField('PlayerClasses', related_name='discipline')
    # player_rankings = rails_models.RelatedField('PlayerRankings', related_name='discipline')
    discipline_cc = models.OneToOneField('DisciplineCc', on_delete=models.CASCADE, related_name='discipline_for_discipline_cc')
    # leagues = rails_models.RelatedField('Leagues', related_name='discipline')
    # game_plan_ccs = rails_models.RelatedField('GamePlanCcs', related_name='discipline')
    # game_plan_row_ccs = rails_models.RelatedField('GamePlanRowCcs', related_name='discipline')
    # seeding_plays = rails_models.RelatedField('SeedingPlays', related_name='discipline')
    competition_cc = models.OneToOneField('CompetitionCc', on_delete=models.CASCADE, related_name='discipline_for_competition_cc')
    branch_cc = models.OneToOneField('BranchCc', on_delete=models.CASCADE, related_name='discipline_for_branch_cc')

    class Meta:
        managed = False
        db_table = 'disciplines'
        unique_together = (('name', 'table_kind_id'), ('name', 'table_kind_id'),)
