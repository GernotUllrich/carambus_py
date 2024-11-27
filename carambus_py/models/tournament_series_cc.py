from django.db import models

class TournamentSeriesCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    branch_cc_id = models.IntegerField(blank=True, null=True)
    season = models.CharField(max_length=255, blank=True, null=True)
    valuation = models.IntegerField(blank=True, null=True)
    series_valuation = models.IntegerField(blank=True, null=True)
    no_tournaments = models.IntegerField(blank=True, null=True)
    point_formula = models.CharField(max_length=255, blank=True, null=True)
    min_points = models.IntegerField(blank=True, null=True)
    point_fraction = models.IntegerField(blank=True, null=True)
    price_money = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=255, blank=True, null=True)
    club_id = models.CharField(max_length=255, blank=True, null=True)
    show_jackpot = models.IntegerField(blank=True, null=True)
    jackpot = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    # tournament_ccs = rails_models.RelatedField('TournamentCcs', related_name='tournamentseriescc')

    class Meta:
        managed = True
        db_table = 'tournament_series_ccs'