from .branch_cc import BranchCc
from .category_cc import CategoryCc
from .championship_type_cc import ChampionshipTypeCc
from .discipline import Discipline
from .group_cc import GroupCc
from .location import Location
from .registration_list_cc import RegistrationListCc
from .tournament import Tournament
from .tournament_series_cc import TournamentSeriesCc
from django.db import models

class TournamentCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    context = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    shortname = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    season = models.CharField(max_length=255, blank=True, null=True)
    registration_rule = models.IntegerField(blank=True, null=True)
    tournament_start = models.DateTimeField(blank=True, null=True)
    tournament_end = models.DateTimeField(blank=True, null=True)
    starting_at = models.TimeField(blank=True, null=True)
    league_climber_quote = models.IntegerField(blank=True, null=True)
    entry_fee = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    max_players = models.IntegerField(blank=True, null=True)
    location_text = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    poster = models.CharField(max_length=255, blank=True, null=True)
    tender = models.CharField(max_length=255, blank=True, null=True)
    flowchart = models.CharField(max_length=255, blank=True, null=True)
    ranking_list = models.CharField(max_length=255, blank=True, null=True)
    successor_list = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    branch_cc_name = models.CharField(max_length=255, blank=True, null=True)
    category_cc_name = models.CharField(max_length=255, blank=True, null=True)
    championship_type_cc_name = models.CharField(max_length=255, blank=True, null=True)
    branch_cc = models.ForeignKey(BranchCc, on_delete=models.CASCADE, related_name='tournament_ccs_for_branch_cc')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='tournament_ccs_for_location')
    registration_list_cc = models.ForeignKey(RegistrationListCc, on_delete=models.CASCADE,
                                             related_name='tournament_ccs_for_registration_list_cc')
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='tournament_ccs_for_discipline')
    group_cc = models.ForeignKey(GroupCc, on_delete=models.CASCADE, related_name='tournament_ccs_for_group_cc')
    championship_type_cc = models.ForeignKey(ChampionshipTypeCc, on_delete=models.CASCADE,
                                             related_name='tournament_ccs_for_championship_type_cc')
    category_cc = models.ForeignKey(CategoryCc, on_delete=models.CASCADE,
                                    related_name='tournament_ccs_for_category_cc')
    tournament_series_cc = models.ForeignKey(TournamentSeriesCc, on_delete=models.CASCADE,
                                             related_name='tournament_ccs_for_tournament_series_cc')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='tournament_cc_for_tournament')

    class Meta:
        managed = True
        db_table = 'tournament_ccs'
        unique_together = (('cc_id', 'context'),)
        if 'test' in sys.argv:
            managed = False
            unique_together = None