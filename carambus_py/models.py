import sys
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import F

__all__ = [
    "Account",
    "AccountInvitation",
    "AccountUser",
    "Addresse",
    "Announcement",
    "ApiToken",
    "BranchCc",
    "CalendarEvent",
    "CategoryCc",
    "ChampionshipTypeCc",
    "Club",
    "ClubLocation",
    "CompetitionCc",
    "ConnectedAccount",
    "Country",
    "DebugInfo",
    "Discipline",
    "DisciplineCc",
    "DisciplinePhase",
    "DisciplineTournamentPlan",
    "Game",
    "GameParticipation",
    "GamePlan",
    "GamePlanCc",
    "GamePlanRowCc",
    "GroupCc",
    "InboundWebhook",
    "IonContent",
    "IonModule",
    "League",
    "LeagueCc",
    "LeagueTeam",
    "LeagueTeamCc",
    "Location",
    "MetaMap",
    "NotificationToken",
    "Party",
    "PartyCc",
    "PartyGame",
    "PartyGameCc",
    "PartyMonitor",
    "Plan",
    "Player",
    "PlayerClass",
    "PlayerRanking",
    "Region",
    "RegionCc",
    "RegistrationCc",
    "RegistrationListCc",
    "Season",
    "SeasonCc",
    "SeasonParticipation",
    "Seeding",
    "Setting",
    "Slot",
    "SyncHash",
    "Table",
    "TableKind",
    "TableLocal",
    "TableMonitor",
    "Tournament",
    "TournamentCc",
    "TournamentLocal",
    "TournamentMonitor",
    "TournamentPlan",
    "TournamentSeriesCc",
    "Upload",
    "User",
    "Version",
]


class Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True, related_name='accounts_for_owner')
    personal = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    account_users_count = models.IntegerField(default=0)  # Counter-Cache-Feld
    extra_billing_info = models.TextField(blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    subdomain = models.CharField(max_length=255, blank=True, null=True)
    billing_email = models.CharField(max_length=255, blank=True, null=True)
    users = models.ManyToManyField(
        'User',
        through='AccountUser',
        related_name='accounts'  # Reverse accessor for User to Account
    )
    class Meta:
        db_table = 'accounts'


class AccountInvitation(models.Model):
    id = models.BigAutoField(primary_key=True)
    invited_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True,
                                   related_name='account_invitations_for_user')
    token = models.CharField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    roles = models.JSONField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    account = models.ForeignKey('Account', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'account_invitations'
        unique_together = (('account', 'email'),)


class AccountUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    account = models.ForeignKey('Account', models.CASCADE, related_name='account_users')
    user = models.ForeignKey('User', models.CASCADE, related_name='account_users')
    roles = models.JSONField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    # Automatically update the counter cache
    def save(self, *args, **kwargs):
        if self._state.adding:  # If this is a new AccountUser
            Account.objects.filter(pk=self.account.pk).update(account_users_count=F('account_users_count') + 1)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        Account.objects.filter(pk=self.account.pk).update(account_users_count=F('account_users_count') - 1)
        super().delete(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'account_users'
        unique_together = (('account', 'user'),)
        if 'test' in sys.argv:
            managed = False
            unique_together = None


class Addresse(models.Model):
    id = models.BigAutoField(primary_key=True)
    addressable_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Polymorphic type
    addressable_id = models.BigIntegerField()
    address_type = models.IntegerField(blank=True, null=True)
    line1 = models.CharField(max_length=255, blank=True, null=True)
    line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    addressable = GenericForeignKey('addressable_type', 'addressable_id')  # Combined polymorphic field

    class Meta:
        managed = True
        db_table = 'addresses'


class Announcement(models.Model):
    id = models.BigAutoField(primary_key=True)
    kind = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'announcements'


class ApiToken(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    token = models.CharField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    transient = models.BooleanField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'api_tokens'


class BranchCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    context = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    # competition_ccs = rails_models.RelatedField('CompetitionCcs', related_name='branchcc')
    # game_plan_ccs = rails_models.RelatedField('GamePlanCcs', related_name='branchcc')
    # group_ccs = rails_models.RelatedField('GroupCcs', related_name='branchcc')
    # registration_list_ccs = rails_models.RelatedField('RegistrationListCcs', related_name='branchcc')
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, related_name='branch_ccs_for_discipline')
    # discipline_ccs = rails_models.RelatedField('DisciplineCcs', related_name='branchcc')
    region_cc = models.ForeignKey('RegionCc', on_delete=models.CASCADE, related_name='branch_ccs_for_region_cc')

    # category_ccs = rails_models.RelatedField('CategoryCcs', related_name='branchcc')
    # championship_type_ccs = rails_models.RelatedField('ChampionshipTypeCcs', related_name='branchcc')

    class Meta:
        managed = True
        db_table = 'branch_ccs'
        unique_together = (('region_cc_id', 'cc_id', 'context'),)
        if 'test' in sys.argv:
            managed = False
            unique_together = None


class CalendarEvent(models.Model):
    id = models.BigAutoField(primary_key=True)
    summary = models.CharField(max_length=255, blank=True, null=True)
    recurring = models.BooleanField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    event_start = models.DateTimeField(blank=True, null=True)
    event_end = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'calendar_events'


class CategoryCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    context = models.CharField(max_length=255, blank=True, null=True)
    max_age = models.IntegerField(blank=True, null=True)
    min_age = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    cc_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    # registration_list_ccs = rails_models.RelatedField('RegistrationListCcs', related_name='categorycc')
    # tournament_ccs = rails_models.RelatedField('TournamentCcs', related_name='categorycc')
    branch_cc = models.ForeignKey('BranchCc', on_delete=models.CASCADE, related_name='category_ccs_for_branch_cc')

    class Meta:
        managed = True
        db_table = 'category_ccs'


class ChampionshipTypeCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    shortname = models.CharField(max_length=255, blank=True, null=True)
    context = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    branch_cc = models.ForeignKey('BranchCc', on_delete=models.CASCADE,
                                  related_name='championship_type_ccs_for_branch_cc')

    class Meta:
        managed = True
        db_table = 'championship_type_ccs'


class Club(models.Model):
    id = models.BigAutoField(primary_key=True)
    ba_id = models.IntegerField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    shortname = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    homepage = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    priceinfo = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    founded = models.CharField(max_length=255, blank=True, null=True)
    dbu_entry = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    cc_id = models.IntegerField(blank=True, null=True)
    dbu_nr = models.IntegerField(blank=True, null=True)
    synonyms = models.TextField(blank=True, null=True)
    source_url = models.CharField(max_length=255, blank=True, null=True)
    sync_date = models.DateTimeField(blank=True, null=True)
    region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name='clubs_for_region')

    # players = rails_models.RelatedField('Players', related_name='club')
    # season_participations = rails_models.RelatedField('SeasonParticipations', related_name='club')
    # players = rails_models.RelatedField('Players', related_name='club')
    # club_locations = rails_models.RelatedField('ClubLocations', related_name='club')
    # locations = rails_models.RelatedField('Locations', related_name='club')
    # organized_tournaments = rails_models.RelatedField('OrganizedTournaments', related_name='club')
    # league_teams = rails_models.RelatedField('LeagueTeams', related_name='club')

    class Meta:
        managed = True
        db_table = 'clubs'


class ClubLocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    club = models.ForeignKey('Club', on_delete=models.CASCADE, related_name='club_locations_for_club')
    location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='club_locations_for_location')

    class Meta:
        managed = True
        db_table = 'club_locations'


class CompetitionCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    context = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    branch_cc = models.ForeignKey('BranchCc', on_delete=models.CASCADE, related_name='competition_ccs_for_branch_cc')
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE,
                                   related_name='competition_ccs_for_discipline')

    # season_ccs = rails_models.RelatedField('SeasonCcs', related_name='competitioncc')

    class Meta:
        managed = True
        db_table = 'competition_ccs'
        unique_together = (('branch_cc_id', 'cc_id', 'context'),)
        if 'test' in sys.argv:
            managed = False
            unique_together = None


class ConnectedAccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    owner_id = models.BigIntegerField(blank=True, null=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    uid = models.CharField(max_length=255, blank=True, null=True)
    refresh_token = models.CharField(max_length=255, blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    auth = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    access_token = models.CharField(max_length=255, blank=True, null=True)
    access_token_secret = models.CharField(max_length=255, blank=True, null=True)
    owner_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    owner = GenericForeignKey('owner_type', 'owner_id')

    class Meta:
        managed = True
        db_table = 'connected_accounts'


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


class DebugInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    info = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'debug_infos'


class Discipline(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    type = models.CharField(max_length=255, blank=True, null=True)
    synonyms = models.TextField(blank=True, null=True)
    team_size = models.IntegerField(blank=True, null=True)
    table_kind = models.ForeignKey('TableKind', on_delete=models.CASCADE, related_name='disciplines_for_table_kind')
    super_discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE,
                                         related_name='disciplines_for_discipline')
    # sub_disciplines = rails_models.RelatedField('SubDisciplines', related_name='discipline')
    # tournaments = rails_models.RelatedField('Tournaments', related_name='discipline')
    # player_classes = rails_models.RelatedField('PlayerClasses', related_name='discipline')
    # player_rankings = rails_models.RelatedField('PlayerRankings', related_name='discipline')
    discipline_cc = models.OneToOneField('DisciplineCc', on_delete=models.CASCADE,
                                         related_name='discipline_for_discipline_cc')
    # leagues = rails_models.RelatedField('Leagues', related_name='discipline')
    # game_plan_ccs = rails_models.RelatedField('GamePlanCcs', related_name='discipline')
    # game_plan_row_ccs = rails_models.RelatedField('GamePlanRowCcs', related_name='discipline')
    # seeding_plays = rails_models.RelatedField('SeedingPlays', related_name='discipline')
    competition_cc = models.OneToOneField('CompetitionCc', on_delete=models.CASCADE,
                                          related_name='discipline_for_competition_cc')
    branch_cc = models.OneToOneField('BranchCc', on_delete=models.CASCADE, related_name='discipline_for_branch_cc')

    class Meta:
        managed = True
        db_table = 'disciplines'
        unique_together = (('name', 'table_kind_id'), ('name', 'table_kind_id'),)
        if 'test' in sys.argv:
            managed = False
            unique_together = None


class DisciplineCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    context = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    branch_cc = models.ForeignKey('BranchCc', on_delete=models.CASCADE, related_name='discipline_ccs_for_branch_cc')
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, related_name='discipline_ccs_for_discipline')

    class Meta:
        managed = True
        db_table = 'discipline_ccs'


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


class DisciplineTournamentPlan(models.Model):
    id = models.BigAutoField(primary_key=True)
    points = models.IntegerField(blank=True, null=True)
    innings = models.IntegerField(blank=True, null=True)
    players = models.IntegerField(blank=True, null=True)
    player_class = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    tournament_plan = models.ForeignKey('TournamentPlan', on_delete=models.CASCADE,
                                        related_name='discipline_tournament_plans_for_tournament_plan')
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE,
                                   related_name='discipline_tournament_plans_for_discipline')

    class Meta:
        managed = True
        db_table = 'discipline_tournament_plans'


class Game(models.Model):
    id = models.BigAutoField(primary_key=True)
    roles = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    seqno = models.IntegerField(blank=True, null=True)
    gname = models.CharField(max_length=255, blank=True, null=True)
    group_no = models.IntegerField(blank=True, null=True)
    table_no = models.IntegerField(blank=True, null=True)
    round_no = models.IntegerField(blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    tournament_type = models.CharField(max_length=255, blank=True, null=True)
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE, related_name='games_for_tournament')
    # game_participations = rails_models.RelatedField('GameParticipations', related_name='game')
    table_monitor = models.OneToOneField('TableMonitor', on_delete=models.CASCADE,
                                         related_name='game_for_table_monitor')
    was_table_monitor = models.OneToOneField('TableMonitor', on_delete=models.CASCADE,
                                             related_name='game_for_was_tournament')

    class Meta:
        managed = True
        db_table = 'games'


class GameParticipation(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    result = models.IntegerField(blank=True, null=True)
    innings = models.IntegerField(blank=True, null=True)
    gd = models.FloatField(blank=True, null=True)
    hs = models.IntegerField(blank=True, null=True)
    gname = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sets = models.IntegerField(blank=True, null=True)
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='game_participations_for_player')
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='game_participations_for_game')

    class Meta:
        managed = True
        db_table = 'game_participations'
        unique_together = (('game_id', 'player_id', 'role'),)
        if 'test' in sys.argv:
            managed = False
            unique_together = None


class GamePlan(models.Model):
    id = models.BigAutoField(primary_key=True)
    footprint = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    # leagues = rails_models.RelatedField('Leagues', related_name='gameplan')

    class Meta:
        managed = True
        db_table = 'game_plans'


class GamePlanCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    mp_won = models.IntegerField(blank=True, null=True)
    mb_draw = models.IntegerField(blank=True, null=True)
    mp_lost = models.IntegerField(blank=True, null=True)
    znp = models.IntegerField(blank=True, null=True)
    vorgabe = models.IntegerField(blank=True, null=True)
    plausi = models.BooleanField(blank=True, null=True)
    pez_partie = models.CharField(max_length=255, blank=True, null=True)
    bez_brett = models.CharField(max_length=255, blank=True, null=True)
    rang_partie = models.IntegerField(blank=True, null=True)
    rang_mgd = models.IntegerField(blank=True, null=True)
    rang_kegel = models.IntegerField(blank=True, null=True)
    ersatzspieler_regel = models.IntegerField(blank=True, null=True)
    row_type_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    branch_cc = models.ForeignKey('BranchCc', on_delete=models.CASCADE, related_name='game_plan_ccs_for_branch_cc')
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, related_name='game_plan_ccs_for_discipline')

    # league_ccs = rails_models.RelatedField('LeagueCcs', related_name='gameplancc')

    class Meta:
        managed = True
        db_table = 'game_plan_ccs'


class GamePlanRowCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    game_plan_id = models.IntegerField(blank=True, null=True)
    home_brett = models.IntegerField(blank=True, null=True)
    visitor_brett = models.IntegerField(blank=True, null=True)
    sets = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    ppg = models.IntegerField(blank=True, null=True)
    ppu = models.IntegerField(blank=True, null=True)
    ppv = models.IntegerField(blank=True, null=True)
    mpg = models.IntegerField(blank=True, null=True)
    pmv = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE,
                                   related_name='game_plan_row_ccs_for_discipline')

    class Meta:
        managed = True
        db_table = 'game_plan_row_ccs'


class GroupCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    context = models.CharField(max_length=255, blank=True, null=True)
    display = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    branch_cc = models.ForeignKey('BranchCc', on_delete=models.CASCADE, related_name='group_ccs_for_branch_cc')

    # tournament_cc = rails_models.RelatedField('TournamentCc', related_name='groupcc')
    # registration_list_ccs = rails_models.RelatedField('RegistrationListCcs', related_name='groupcc')

    class Meta:
        managed = True
        db_table = 'group_ccs'


class InboundWebhook(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.IntegerField()
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'inbound_webhooks'


class IonContent(models.Model):
    id = models.BigAutoField(primary_key=True)
    page_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    level = models.CharField(max_length=255, blank=True, null=True)
    scraped_at = models.DateTimeField(blank=True, null=True)
    deep_scraped_at = models.DateTimeField(blank=True, null=True)
    ion_content_id = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.BooleanField()

    # ion_modules = rails_models.RelatedField('IonModules', related_name='ioncontent')

    class Meta:
        managed = True
        db_table = 'ion_contents'


class IonModule(models.Model):
    id = models.BigAutoField(primary_key=True)
    module_id = models.CharField(max_length=255, blank=True, null=True)
    module_type = models.CharField(max_length=255, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    ion_content = models.ForeignKey('IonContent', on_delete=models.CASCADE, related_name='ion_modules_for_ion_content')

    class Meta:
        managed = True
        db_table = 'ion_modules'


class League(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    registration_until = models.DateField(blank=True, null=True)
    organizer_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Polymorphic type
    organizer_id = models.IntegerField(blank=True, null=True)
    ba_id = models.IntegerField(blank=True, null=True)
    ba_id2 = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    staffel_text = models.CharField(max_length=255, blank=True, null=True)
    cc_id = models.IntegerField(blank=True, null=True)
    shortname = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    source_url = models.CharField(max_length=255, blank=True, null=True)
    sync_date = models.DateTimeField(blank=True, null=True)
    cc_id2 = models.IntegerField(blank=True, null=True)
    game_parameters = models.TextField(blank=True, null=True)
    game_plan_locked = models.BooleanField()
    # league_teams = rails_models.RelatedField('LeagueTeams', related_name='league')
    # parties = rails_models.RelatedField('Parties', related_name='league')
    # tournaments = rails_models.RelatedField('Tournaments', related_name='league')
    tournament = GenericForeignKey('organizer_type', 'organizer_id')  # Combined polymorphic field
    game_plan = models.ForeignKey('GamePlan', on_delete=models.CASCADE, related_name='leagues_for_game_plan')
    region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name='leagues_for_region')
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, related_name='leagues_for_discipline')
    season = models.ForeignKey('Season', on_delete=models.CASCADE, related_name='leagues_for_season')
    league_cc = models.OneToOneField('LeagueCc', on_delete=models.CASCADE, related_name='league_for_league_cc')

    class Meta:
        managed = True
        db_table = 'leagues'
        unique_together = (('ba_id', 'ba_id2'),)
        if 'test' in sys.argv:
            managed = False
            unique_together = None


class LeagueCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    context = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    shortname = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    report_form = models.CharField(max_length=255, blank=True, null=True)
    report_form_data = models.CharField(max_length=255, blank=True, null=True)
    cc_id2 = models.IntegerField(blank=True, null=True)
    season_cc = models.ForeignKey('SeasonCc', on_delete=models.CASCADE, related_name='league_ccs_for_season_cc')
    league = models.ForeignKey('League', on_delete=models.CASCADE, related_name='league_ccs_for_league')
    game_plan_cc = models.ForeignKey('GamePlanCc', on_delete=models.CASCADE, related_name='league_ccs_for_game_plan_cc')

    # league_team_ccs = rails_models.RelatedField('LeagueTeamCcs', related_name='leaguecc')
    # party_ccs = rails_models.RelatedField('PartyCcs', related_name='leaguecc')

    class Meta:
        managed = True
        db_table = 'league_ccs'


class LeagueTeam(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    shortname = models.CharField(max_length=255, blank=True, null=True)
    ba_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    source_url = models.CharField(max_length=255, blank=True, null=True)
    sync_date = models.DateTimeField(blank=True, null=True)
    cc_id = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    league = models.ForeignKey('League', on_delete=models.CASCADE, related_name='league_teams_for_league')
    club = models.ForeignKey('Club', on_delete=models.CASCADE, related_name='league_teams_for_club')
    # parties_a = rails_models.RelatedField('PartiesA', related_name='leagueteam')
    # parties_b = rails_models.RelatedField('PartiesB', related_name='leagueteam')
    # parties_as_host = rails_models.RelatedField('PartiesAsHost', related_name='leagueteam')
    # no_show_parties = rails_models.RelatedField('NoShowParties', related_name='leagueteam')
    league_team_cc = models.OneToOneField('LeagueTeamCc', on_delete=models.CASCADE,
                                          related_name='league_team_for_league_team_cc')

    # seedings = rails_models.RelatedField('Seedings', related_name='leagueteam')

    class Meta:
        managed = True
        db_table = 'league_teams'


class LeagueTeamCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    shortname = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    league_cc = models.ForeignKey('LeagueCc', on_delete=models.CASCADE, related_name='league_team_ccs_for_league_cc')
    league_team = models.ForeignKey('LeagueTeam', on_delete=models.CASCADE,
                                    related_name='league_team_ccs_for_league_team')

    # party_a_ccs = rails_models.RelatedField('PartyACcs', related_name='leagueteamcc')
    # party_b_ccs = rails_models.RelatedField('PartyBCcs', related_name='leagueteamcc')
    # party_host_ccs = rails_models.RelatedField('PartyHostCcs', related_name='leagueteamcc')

    class Meta:
        managed = True
        db_table = 'league_team_ccs'


class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    organizer_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Polymorphic type
    organizer_id = models.IntegerField(blank=True, null=True)
    md5 = models.CharField(unique=True)
    synonyms = models.TextField(blank=True, null=True)
    source_url = models.CharField(max_length=255, blank=True, null=True)
    sync_date = models.DateTimeField(blank=True, null=True)
    cc_id = models.IntegerField(blank=True, null=True)
    dbu_nr = models.IntegerField(blank=True, null=True)
    club = models.ForeignKey('Club', on_delete=models.CASCADE, related_name='locations_for_club')
    # club_locations = rails_models.RelatedField('ClubLocations', related_name='location')
    # clubs = rails_models.RelatedField('Clubs', related_name='location')
    # parties = rails_models.RelatedField('Parties', related_name='location')
    region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name='locations_for_region')
    organizer = GenericForeignKey('organizer_type', 'organizer_id')  # Combined polymorphic field

    # tables = rails_models.RelatedField('Tables', related_name='location')
    # tournaments = rails_models.RelatedField('Tournaments', related_name='location')

    class Meta:
        managed = True
        db_table = 'locations'


class MetaMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    class_ba = models.CharField(max_length=255, blank=True, null=True)
    class_cc = models.CharField(max_length=255, blank=True, null=True)
    ba_base_url = models.CharField(max_length=255, blank=True, null=True)
    cc_base_url = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'meta_maps'  # your_project/tests/utils/models_import_helper.py


class NotificationToken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'notification_tokens'


class Party(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    ba_id = models.IntegerField(blank=True, null=True)
    day_seqno = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    section = models.CharField(max_length=255, blank=True, null=True)
    cc_id = models.IntegerField(blank=True, null=True)
    register_at = models.DateField(blank=True, null=True)
    group = models.CharField(max_length=255, blank=True, null=True)
    round = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    source_url = models.CharField(max_length=255, blank=True, null=True)
    sync_date = models.DateTimeField(blank=True, null=True)
    reported_at = models.DateTimeField(blank=True, null=True)
    reported_by_player_id = models.IntegerField(blank=True, null=True)
    reported_by = models.CharField(max_length=255, blank=True, null=True)
    party_no = models.IntegerField(blank=True, null=True)
    manual_assignment = models.BooleanField(blank=True, null=True)
    continuous_placements = models.BooleanField()
    timeout = models.IntegerField()
    timeouts = models.IntegerField(blank=True, null=True)
    time_out_stoke_preparation_sec = models.IntegerField(blank=True, null=True)
    time_out_warm_up_first_min = models.IntegerField(blank=True, null=True)
    time_out_warm_up_follow_up_min = models.IntegerField(blank=True, null=True)
    sets_to_play = models.IntegerField()
    sets_to_win = models.IntegerField()
    team_size = models.IntegerField()
    fixed_display_left = models.CharField(max_length=255, blank=True, null=True)
    allow_follow_up = models.BooleanField()
    color_remains_with_set = models.BooleanField()
    kickoff_switches_with = models.CharField(max_length=255, blank=True, null=True)
    league = models.ForeignKey('League', on_delete=models.CASCADE, related_name='parties_for_league')
    # games = rails_models.RelatedField('Games', related_name='party')
    league_team_a = models.ForeignKey('LeagueTeam', on_delete=models.CASCADE, related_name='parties_for_league_team_a')
    league_team_b = models.ForeignKey('LeagueTeam', on_delete=models.CASCADE,
                                      related_name='parties_for_league_for_league_team_b')
    host_league_team = models.ForeignKey('LeagueTeam', on_delete=models.CASCADE,
                                         related_name='parties_for_host_league_team')
    location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='parties_for_location')
    no_show_team = models.ForeignKey('LeagueTeam', on_delete=models.CASCADE, related_name='parties_for_no_show_team')
    party_monitor = models.OneToOneField('PartyMonitor', on_delete=models.CASCADE,
                                         related_name='party_for_party_monitor')
    party_cc = models.OneToOneField('PartyCc', on_delete=models.CASCADE, related_name='party_for_party_cc')

    # party_games = rails_models.RelatedField('PartyGames', related_name='party')
    # seedings = rails_models.RelatedField('Seedings', related_name='party')

    class Meta:
        managed = True
        db_table = 'parties'


class PartyCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    day_seqno = models.IntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    register_at = models.DateField(blank=True, null=True)
    group = models.CharField(max_length=255, blank=True, null=True)
    round = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    match_id = models.IntegerField(blank=True, null=True)
    league_cc = models.ForeignKey('LeagueCc', on_delete=models.CASCADE, related_name='party_ccs_for_league_cc')
    league_team_a_cc = models.ForeignKey('LeagueTeamCc', on_delete=models.CASCADE,
                                         related_name='party_ccs_for_league_team_a_cc')
    league_team_b_cc = models.ForeignKey('LeagueTeamCc', on_delete=models.CASCADE,
                                         related_name='party_ccs_for_league_team_b_cc')
    league_team_host_cc = models.ForeignKey('LeagueTeamCc', on_delete=models.CASCADE,
                                            related_name='party_ccs_for_league_team_host_cc')
    party = models.ForeignKey('Party', on_delete=models.CASCADE, related_name='party_cc_for_party')

    # party_game_ccs = rails_models.RelatedField('PartyGameCcs', related_name='partycc')

    class Meta:
        managed = True
        db_table = 'party_ccs'


class PartyGame(models.Model):
    id = models.BigAutoField(primary_key=True)
    seqno = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    data = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    party = models.ForeignKey('Party', on_delete=models.CASCADE, related_name='party_games_for_party')
    player_a = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='party_games_for_player_a')
    player_b = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='party_games_for_player_b')
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, related_name='party_games_for_discipline')
    party_game_cc = models.OneToOneField('PartyGameCc', on_delete=models.CASCADE,
                                         related_name='party_game_for_party_game_cc')

    class Meta:
        managed = True
        db_table = 'party_games'


class PartyGameCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    seqno = models.IntegerField(blank=True, null=True)
    player_a_id = models.IntegerField(blank=True, null=True)
    player_b_id = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    discipline_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    party_cc = models.ForeignKey('PartyCc', on_delete=models.CASCADE, related_name='party_game_ccs_for_party_cc')
    party_game = models.ForeignKey('PartyGame', on_delete=models.CASCADE, related_name='party_game_cc_for_party_game')

    class Meta:
        managed = True
        db_table = 'party_game_ccs'


class PartyMonitor(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    timeout = models.IntegerField()
    timeouts = models.IntegerField(blank=True, null=True)
    time_out_stoke_preparation_sec = models.IntegerField(blank=True, null=True)
    time_out_warm_up_first_min = models.IntegerField(blank=True, null=True)
    time_out_warm_up_follow_up_min = models.IntegerField(blank=True, null=True)
    sets_to_play = models.IntegerField()
    sets_to_win = models.IntegerField()
    team_size = models.IntegerField()
    fixed_display_left = models.CharField(max_length=255, blank=True, null=True)
    allow_follow_up = models.BooleanField()
    color_remains_with_set = models.BooleanField()
    kickoff_switches_with = models.CharField(max_length=255, blank=True, null=True)
    party = models.ForeignKey('Party', on_delete=models.CASCADE, related_name='party_monitor_for_party')

    # table_monitors = rails_models.RelatedField('TableMonitors', related_name='partymonitor')

    class Meta:
        managed = True
        db_table = 'party_monitors'


class Plan(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    interval = models.CharField(max_length=255)
    details = models.JSONField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    trial_period_days = models.IntegerField(blank=True, null=True)
    hidden = models.BooleanField(blank=True, null=True)
    currency = models.CharField(max_length=255, blank=True, null=True)
    interval_count = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    unit_label = models.CharField(max_length=255, blank=True, null=True)
    charge_per_unit = models.BooleanField(blank=True, null=True)
    stripe_id = models.CharField(max_length=255, blank=True, null=True)
    braintree_id = models.CharField(max_length=255, blank=True, null=True)
    paddle_billing_id = models.CharField(max_length=255, blank=True, null=True)
    paddle_classic_id = models.CharField(max_length=255, blank=True, null=True)
    lemon_squeezy_id = models.CharField(max_length=255, blank=True, null=True)
    fake_processor_id = models.CharField(max_length=255, blank=True, null=True)
    contact_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plans'


class Player(models.Model):
    id = models.BigAutoField(primary_key=True)
    ba_id = models.IntegerField(unique=True, blank=True, null=True)
    club_id = models.IntegerField(blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    guest = models.BooleanField()
    nickname = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    tournament_id = models.IntegerField(blank=True, null=True)
    cc_id = models.IntegerField(blank=True, null=True)
    dbu_nr = models.IntegerField(blank=True, null=True)
    dbu_pass_nr = models.IntegerField(blank=True, null=True)
    fl_name = models.CharField(max_length=255, blank=True, null=True)
    source_url = models.CharField(max_length=255, blank=True, null=True)
    sync_date = models.DateTimeField(blank=True, null=True)
    nrw_nr = models.IntegerField(blank=True, null=True)
    pin4 = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)

    # game_participations = rails_models.RelatedField('GameParticipations', related_name='player')
    # season_participations = rails_models.RelatedField('SeasonParticipations', related_name='player')
    # clubs = rails_models.RelatedField('Clubs', related_name='player')
    # player_rankings = rails_models.RelatedField('PlayerRankings', related_name='player')
    # seedings = rails_models.RelatedField('Seedings', related_name='player')
    # registration_ccs = rails_models.RelatedField('RegistrationCcs', related_name='player')
    # party_a_games = rails_models.RelatedField('PartyAGames', related_name='player')
    # party_b_games = rails_models.RelatedField('PartyBGames', related_name='player')
    # admin_user = models_xxx.OneToOneField(User, on_delete=models_xxx.CASCADE, related_name='player_for_user')

    class Meta:
        managed = True
        db_table = 'players'


class PlayerClass(models.Model):
    id = models.BigAutoField(primary_key=True)
    shortname = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, related_name='player_classes_for_discipline')

    # player_rankings = rails_models.RelatedField('PlayerRankings', related_name='playerclass')
    # p_player_rankings = rails_models.RelatedField('PPlayerRankings', related_name='playerclass')
    # pp_player_rankings = rails_models.RelatedField('PpPlayerRankings', related_name='playerclass')
    # tournament_player_rankings = rails_models.RelatedField('TournamentPlayerRankings', related_name='playerclass')

    class Meta:
        managed = True
        db_table = 'player_classes'


class PlayerRanking(models.Model):
    id = models.BigAutoField(primary_key=True)
    org_level = models.CharField(max_length=255, blank=True, null=True)
    innings = models.IntegerField(blank=True, null=True)
    tournament_player_class_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    gd = models.FloatField(blank=True, null=True)
    hs = models.IntegerField(blank=True, null=True)
    bed = models.FloatField(blank=True, null=True)
    btg = models.FloatField(blank=True, null=True)
    p_gd = models.FloatField(blank=True, null=True)
    pp_gd = models.FloatField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    g = models.IntegerField(blank=True, null=True)
    v = models.IntegerField(blank=True, null=True)
    quote = models.FloatField(blank=True, null=True)
    sp_g = models.IntegerField(blank=True, null=True)
    sp_v = models.IntegerField(blank=True, null=True)
    sp_quote = models.FloatField(blank=True, null=True)
    balls = models.IntegerField(blank=True, null=True)
    sets = models.IntegerField(blank=True, null=True)
    t_ids = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE,
                                   related_name='player_rankings_for_discipline')
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player_rankings_for_player')
    region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name='player_rankings_for_region')
    season = models.ForeignKey('Season', on_delete=models.CASCADE, related_name='player_rankings_for_season')
    player_class = models.ForeignKey('PlayerClass', on_delete=models.CASCADE,
                                     related_name='player_rankings_for_player_class')
    p_player_class = models.ForeignKey('PlayerClass', on_delete=models.CASCADE,
                                       related_name='player_rankings_for_p_player_class')
    pp_player_class = models.ForeignKey('PlayerClass', on_delete=models.CASCADE,
                                        related_name='player_rankings_for_pp_player_class')

    class Meta:
        managed = True
        db_table = 'player_rankings'


class Region(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    shortname = models.CharField(unique=True, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    public_cc_url_base = models.CharField(max_length=255, blank=True, null=True)
    dbu_name = models.CharField(max_length=255, blank=True, null=True)
    telefon = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    opening = models.CharField(max_length=255, blank=True, null=True)
    source_url = models.CharField(max_length=255, blank=True, null=True)
    sync_date = models.DateTimeField(blank=True, null=True)
    cc_id = models.IntegerField(blank=True, null=True)
    scrape_data = models.TextField(blank=True, null=True)

    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='regions_for_country')
    # clubs = rails_models.RelatedField('Clubs', related_name='region')
    # tournaments = rails_models.RelatedField('Tournaments', related_name='region')
    # player_rankings = rails_models.RelatedField('PlayerRankings', related_name='region')
    # locations = rails_models.RelatedField('Locations', related_name='region')
    # organized_tournaments = rails_models.RelatedField('OrganizedTournaments', related_name='region')
    # organized_leagues = rails_models.RelatedField('OrganizedLeagues', related_name='region')
    setting = models.OneToOneField('Setting', on_delete=models.CASCADE, related_name='region_for_setting')
    # leagues = rails_models.RelatedField('Leagues', related_name='region')
    region_cc = models.OneToOneField('RegionCc', on_delete=models.CASCADE, related_name='region_for_region_cc')

    class Meta:
        managed = True
        db_table = 'regions'


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
    region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name='region_ccs_for_region')

    # branch_ccs = rails_models.RelatedField('BranchCcs', related_name='regioncc')

    class Meta:
        managed = True
        db_table = 'region_ccs'
        unique_together = (('cc_id', 'context'),)
        if 'test' in sys.argv:
            managed = False
            unique_together = None


class RegistrationCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='registration_ccs_for_player')
    registration_list_cc = models.ForeignKey('RegistrationListCc', on_delete=models.CASCADE,
                                             related_name='registration_ccs_for_registration_list_cc')

    class Meta:
        managed = True
        db_table = 'registration_ccs'
        unique_together = (('player_id', 'registration_list_cc_id'),)
        if 'test' in sys.argv:
            managed = False
            unique_together = None


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
    branch_cc = models.ForeignKey('BranchCc', on_delete=models.CASCADE,
                                  related_name='registration_list_ccs_for_branch_cc')
    season = models.ForeignKey('Season', on_delete=models.CASCADE, related_name='registration_list_ccs_for_season')
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE,
                                   related_name='registration_list_ccs_for_discipline')
    category_cc = models.ForeignKey('CategoryCc', on_delete=models.CASCADE,
                                    related_name='registration_list_ccs_for_category_cc')

    # registration_ccs = rails_models.RelatedField('RegistrationCcs', related_name='registrationlistcc')

    class Meta:
        managed = True
        db_table = 'registration_list_ccs'


class Season(models.Model):
    id = models.BigAutoField(primary_key=True)
    ba_id = models.IntegerField(unique=True, blank=True, null=True)
    name = models.CharField(unique=True, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    # tournaments = rails_models.RelatedField('Tournaments', related_name='season')
    # season_participations = rails_models.RelatedField('SeasonParticipations', related_name='season')
    # player_rankings = rails_models.RelatedField('PlayerRankings', related_name='season')
    # season_ccs = rails_models.RelatedField('SeasonCcs', related_name='season')
    # leagues = rails_models.RelatedField('Leagues', related_name='season')

    class Meta:
        managed = True
        db_table = 'seasons'


class SeasonCc(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    context = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    competition_cc = models.ForeignKey('CompetitionCc', on_delete=models.CASCADE,
                                       related_name='season_cc_for_competition_cc')
    season = models.ForeignKey('Season', on_delete=models.CASCADE, related_name='season_cc_for_season')

    # league_ccs = rails_models.RelatedField('LeagueCcs', related_name='seasoncc')
    # registration_list_ccs = rails_models.RelatedField('RegistrationListCcs', related_name='seasoncc')

    class Meta:
        managed = True
        db_table = 'season_ccs'
        unique_together = (('competition_cc_id', 'cc_id', 'context'),)
        if 'test' in sys.argv:
            managed = False
            unique_together = None


class SeasonParticipation(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.CharField(max_length=255, blank=True, null=True)
    ba_id = models.IntegerField(blank=True, null=True)
    source_url = models.CharField(max_length=255, blank=True, null=True)
    sync_date = models.DateTimeField(blank=True, null=True)
    season = models.ForeignKey('Season', on_delete=models.CASCADE, related_name='season_participations_for_season')
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='season_participations_for_player')
    club = models.ForeignKey('Club', on_delete=models.CASCADE, related_name='season_participations_for_club')

    class Meta:
        managed = True
        db_table = 'season_participations'
        unique_together = (('player_id', 'club_id', 'season_id'),)
        if 'test' in sys.argv:
            managed = False
            unique_together = None


class Seeding(models.Model):
    id = models.BigAutoField(primary_key=True)
    ba_state = models.CharField(max_length=255, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    balls_goal = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    rank = models.IntegerField(blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)

    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='seedings_for_player')
    playing_discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE,
                                           related_name='seedings_for_discipline')
    league_team = models.ForeignKey('LeagueTeam', on_delete=models.CASCADE, related_name='seedings_for_league_team')

    tournament_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Polymorphic type
    tournament_id = models.PositiveIntegerField()  # Polymorphic object ID
    tournament = GenericForeignKey('tournament_type', 'tournament_id')  # Combined polymorphic field

    class Meta:
        managed = True
        ordering = ['position']  # Order by position ascending
        db_table = 'seedings'


class Setting(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name='settings_for_region')
    club = models.ForeignKey('Club', on_delete=models.CASCADE, related_name='settings_for_club')
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE, related_name='settings_for_tournament')

    class Meta:
        managed = True
        db_table = 'settings'


class Slot(models.Model):
    id = models.BigAutoField(primary_key=True)
    dayofweek = models.IntegerField(blank=True, null=True)
    hourofday_start = models.IntegerField(blank=True, null=True)
    minuteofhour_start = models.IntegerField(blank=True, null=True)
    hourofday_end = models.IntegerField(blank=True, null=True)
    minuteofhour_end = models.IntegerField(blank=True, null=True)
    next_start = models.DateTimeField(blank=True, null=True)
    next_end = models.DateTimeField(blank=True, null=True)
    table_id = models.IntegerField(blank=True, null=True)
    recurring = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'slots'


class SyncHash(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    md5 = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    doc = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sync_hashes'


class Table(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    ip_address = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    tpl_ip_address = models.IntegerField(blank=True, null=True)
    event_id = models.CharField(max_length=255, blank=True, null=True)
    event_summary = models.CharField(max_length=255, blank=True, null=True)
    event_creator = models.CharField(max_length=255, blank=True, null=True)
    event_start = models.DateTimeField(blank=True, null=True)
    event_end = models.DateTimeField(blank=True, null=True)
    heater_on_reason = models.CharField(max_length=255, blank=True, null=True)
    heater_off_reason = models.CharField(max_length=255, blank=True, null=True)
    heater_switched_on_at = models.DateTimeField(blank=True, null=True)
    heater_switched_off_at = models.DateTimeField(blank=True, null=True)
    heater = models.BooleanField(blank=True, null=True)
    manual_heater_on_at = models.DateTimeField(blank=True, null=True)
    manual_heater_off_at = models.DateTimeField(blank=True, null=True)
    scoreboard = models.BooleanField(blank=True, null=True)
    scoreboard_on_at = models.DateTimeField(blank=True, null=True)
    scoreboard_off_at = models.DateTimeField(blank=True, null=True)
    heater_auto = models.BooleanField(blank=True, null=True)
    location = models.ForeignKey('Location', models.DO_NOTHING, blank=True, null=True,
                                 related_name='tables_for_location')
    table_kind = models.ForeignKey('TableKind', models.DO_NOTHING, blank=True, null=True,
                                   related_name='tables_for_table_kind')
    table_monitor = models.ForeignKey('TableMonitor', on_delete=models.DO_NOTHING,
                                      related_name='table_for_table_monitor')
    table_local = models.OneToOneField('TableLocal', on_delete=models.CASCADE, related_name='table_for_table_local')

    class Meta:
        managed = True
        db_table = 'tables'


class TableKind(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    short = models.CharField(max_length=255, blank=True, null=True)
    measures = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    # disciplines = rails_models.RelatedField('Disciplines', related_name='tablekind')
    # tables = rails_models.RelatedField('Tables', related_name='tablekind')

    class Meta:
        managed = True
        db_table = 'table_kinds'


class TableLocal(models.Model):
    id = models.BigAutoField(primary_key=True)
    tpl_ip_address = models.CharField(max_length=255, blank=True, null=True)
    ip_address = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    event_id = models.CharField(max_length=255, blank=True, null=True)
    event_summary = models.CharField(max_length=255, blank=True, null=True)
    event_creator = models.CharField(max_length=255, blank=True, null=True)
    event_start = models.DateTimeField(blank=True, null=True)
    event_end = models.DateTimeField(blank=True, null=True)
    heater_on_reason = models.CharField(max_length=255, blank=True, null=True)
    heater_off_reason = models.CharField(max_length=255, blank=True, null=True)
    heater_switched_on_at = models.DateTimeField(blank=True, null=True)
    heater_switched_off_at = models.DateTimeField(blank=True, null=True)
    heater = models.BooleanField(blank=True, null=True)
    manual_heater_on_at = models.DateTimeField(blank=True, null=True)
    manual_heater_off_at = models.DateTimeField(blank=True, null=True)
    scoreboard = models.BooleanField(blank=True, null=True)
    scoreboard_on_at = models.DateTimeField(blank=True, null=True)
    scoreboard_off_at = models.DateTimeField(blank=True, null=True)
    table = models.ForeignKey('Table', on_delete=models.CASCADE, related_name='table_local_for_table')

    class Meta:
        managed = True
        db_table = 'table_locals'


class TableMonitor(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    next_game_id = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    ip_address = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    active_timer = models.CharField(max_length=255, blank=True, null=True)
    timer_start_at = models.DateTimeField(blank=True, null=True)
    timer_finish_at = models.DateTimeField(blank=True, null=True)
    timer_halt_at = models.DateTimeField(blank=True, null=True)
    nnn = models.IntegerField(blank=True, null=True)
    panel_state = models.CharField(max_length=255)
    current_element = models.CharField(max_length=255)
    timer_job_id = models.CharField(max_length=255, blank=True, null=True)
    clock_job_id = models.CharField(max_length=255, blank=True, null=True)
    copy_from = models.IntegerField(blank=True, null=True)
    tournament_monitor_type = models.CharField(max_length=255, blank=True, null=True)
    prev_data = models.TextField(blank=True, null=True)
    prev_tournament_monitor_id = models.IntegerField(blank=True, null=True)
    prev_tournament_monitor_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Polymorphic type
    tournament_monitor = models.ForeignKey('TournamentMonitor', on_delete=models.CASCADE,
                                           related_name='table_monitors_for_tournament_monitor')
    game = models.ForeignKey('Game', on_delete=models.SET_NULL, null=True, related_name='table_monitor_for_game')
    prev_game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='table_monitors_for_prev_game')
    prev_tournament_monitor = GenericForeignKey('prev_tournament_monitor_type',
                                                'prev_tournament_monitor_id')  # Combined polymorphic field
    table = models.OneToOneField('Table', on_delete=models.CASCADE, related_name='table_monitors_for_table')

    class Meta:
        managed = True
        db_table = 'table_monitors'


class Tournament(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    modus = models.CharField(max_length=255, blank=True, null=True)
    age_restriction = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    accredation_end = models.DateTimeField(blank=True, null=True)
    location_text = models.TextField(blank=True, null=True)
    ba_id = models.IntegerField(unique=True, blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    plan_or_show = models.CharField(max_length=255, blank=True, null=True)
    single_or_league = models.CharField(max_length=255, blank=True, null=True)
    shortname = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    ba_state = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    sync_date = models.DateTimeField(blank=True, null=True)
    player_class = models.CharField(max_length=255, blank=True, null=True)
    innings_goal = models.IntegerField(blank=True, null=True)
    balls_goal = models.IntegerField(blank=True, null=True)
    handicap_tournier = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    timeout = models.IntegerField(blank=True, null=True)
    time_out_warm_up_first_min = models.IntegerField(blank=True, null=True)
    time_out_warm_up_follow_up_min = models.IntegerField(blank=True, null=True)
    organizer_id = models.IntegerField(blank=True, null=True)
    organizer_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Polymorphic type
    timeouts = models.IntegerField()
    admin_controlled = models.BooleanField()
    gd_has_prio = models.BooleanField()
    sets_to_win = models.IntegerField()
    sets_to_play = models.IntegerField()
    team_size = models.IntegerField()
    fixed_display_left = models.CharField(max_length=255, blank=True, null=True)
    color_remains_with_set = models.BooleanField()
    allow_follow_up = models.BooleanField()
    continuous_placements = models.BooleanField()
    manual_assignment = models.BooleanField(blank=True, null=True)
    kickoff_switches_with = models.CharField(max_length=255, blank=True, null=True)
    source_url = models.CharField(max_length=255, blank=True, null=True)
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, related_name='tournaments_for_discipline')
    region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name='tournaments_for_region')
    season = models.ForeignKey('Season', on_delete=models.CASCADE, related_name='tournaments_for_season')
    tournament_plan = models.ForeignKey('TournamentPlan', on_delete=models.CASCADE,
                                        related_name='tournaments_for_tournament_plan')
    league = models.ForeignKey('League', on_delete=models.CASCADE, related_name='tournaments_for_league')
    # seedings = rails_models.RelatedField('Seedings', related_name='tournament')
    # games = rails_models.RelatedField('Games', related_name='tournament')
    # teams = rails_models.RelatedField('Teams', related_name='tournament')
    tournament_monitor = models.OneToOneField('TournamentMonitor', on_delete=models.CASCADE,
                                              related_name='tournament_for_tournament_monitor')
    tournament_cc = models.OneToOneField('TournamentCc', on_delete=models.CASCADE,
                                         related_name='tournament_for_tournament_cc')
    setting = models.OneToOneField('Setting', on_delete=models.CASCADE, related_name='tournaments_for_setting')
    organizer = GenericForeignKey('organizer_type', 'organizer_id')  # Combined polymorphic field
    location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='tournaments_for_location')
    tournament_local = models.OneToOneField('TournamentLocal', on_delete=models.CASCADE,
                                            related_name='tournament_for_tournament_local')

    class Meta:
        managed = True
        db_table = 'tournaments'


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
    branch_cc = models.ForeignKey('BranchCc', on_delete=models.CASCADE, related_name='tournament_ccs_for_branch_cc')
    location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='tournament_ccs_for_location')
    registration_list_cc = models.ForeignKey('RegistrationListCc', on_delete=models.CASCADE,
                                             related_name='tournament_ccs_for_registration_list_cc')
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, related_name='tournament_ccs_for_discipline')
    group_cc = models.ForeignKey('GroupCc', on_delete=models.CASCADE, related_name='tournament_ccs_for_group_cc')
    championship_type_cc = models.ForeignKey('ChampionshipTypeCc', on_delete=models.CASCADE,
                                             related_name='tournament_ccs_for_championship_type_cc')
    category_cc = models.ForeignKey('CategoryCc', on_delete=models.CASCADE,
                                    related_name='tournament_ccs_for_category_cc')
    tournament_series_cc = models.ForeignKey('TournamentSeriesCc', on_delete=models.CASCADE,
                                             related_name='tournament_ccs_for_tournament_series_cc')
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE, related_name='tournament_cc_for_tournament')

    class Meta:
        managed = True
        db_table = 'tournament_ccs'
        unique_together = (('cc_id', 'context'),)
        if 'test' in sys.argv:
            managed = False
            unique_together = None


class TournamentLocal(models.Model):
    id = models.BigAutoField(primary_key=True)
    timeout = models.IntegerField(blank=True, null=True)
    timeouts = models.IntegerField(blank=True, null=True)
    admin_controlled = models.BooleanField(blank=True, null=True)
    gd_has_prio = models.BooleanField(blank=True, null=True)
    sets_to_win = models.IntegerField()
    sets_to_play = models.IntegerField()
    team_size = models.IntegerField()
    fixed_display_left = models.CharField(max_length=255, blank=True, null=True)
    color_remains_with_set = models.BooleanField()
    allow_follow_up = models.BooleanField()
    kickoff_switches_with = models.CharField(max_length=255, blank=True, null=True)
    innings_goal = models.IntegerField(blank=True, null=True)
    balls_goal = models.IntegerField(blank=True, null=True)
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE,
                                   related_name='tournament_local_for_tournament')

    class Meta:
        managed = True
        db_table = 'tournament_locals'


class TournamentMonitor(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    innings_goal = models.IntegerField(blank=True, null=True)
    balls_goal = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    timeouts = models.IntegerField(blank=True, null=True)
    timeout = models.IntegerField()
    sets_to_win = models.IntegerField()
    sets_to_play = models.IntegerField()
    fixed_display_left = models.CharField(max_length=255, blank=True, null=True)
    color_remains_with_set = models.BooleanField()
    team_size = models.IntegerField()
    allow_follow_up = models.BooleanField()
    allow_overflow = models.BooleanField(blank=True, null=True)
    kickoff_switches_with = models.CharField(max_length=255, blank=True, null=True)
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE,
                                   related_name='tournament_monitor_for_tournament')

    # table_monitors = rails_models.RelatedField('TableMonitors', related_name='tournamentmonitor')
    # was_table_monitors = rails_models.RelatedField('WasTableMonitors', related_name='tournamentmonitor')

    class Meta:
        managed = True
        db_table = 'tournament_monitors'


class TournamentPlan(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    rulesystem = models.TextField(blank=True, null=True)
    players = models.IntegerField(blank=True, null=True)
    tables = models.IntegerField(blank=True, null=True)
    more_description = models.TextField(blank=True, null=True)
    even_more_description = models.TextField(blank=True, null=True)
    executor_class = models.CharField(max_length=255, blank=True, null=True)
    executor_params = models.TextField(blank=True, null=True)
    ngroups = models.IntegerField(blank=True, null=True)
    nrepeats = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    # discipline_tournament_plans = rails_models.RelatedField('DisciplineTournamentPlans', related_name='tournamentplan')
    # tournaments = rails_models.RelatedField('Tournaments', related_name='tournamentplan')

    class Meta:
        managed = True
        db_table = 'tournament_plans'


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


class Upload(models.Model):
    id = models.BigAutoField(primary_key=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'uploads'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True)
    encrypted_password = models.CharField(max_length=255)
    reset_password_token = models.CharField(unique=True, blank=True, null=True)
    reset_password_sent_at = models.DateTimeField(blank=True, null=True)
    remember_created_at = models.DateTimeField(blank=True, null=True)
    confirmation_token = models.CharField(unique=True, blank=True, null=True)
    confirmed_at = models.DateTimeField(blank=True, null=True)
    confirmation_sent_at = models.DateTimeField(blank=True, null=True)
    unconfirmed_email = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    time_zone = models.CharField(max_length=255, blank=True, null=True)
    accepted_terms_at = models.DateTimeField(blank=True, null=True)
    accepted_privacy_at = models.DateTimeField(blank=True, null=True)
    announcements_read_at = models.DateTimeField(blank=True, null=True)
    admin = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    invitation_token = models.CharField(unique=True, blank=True, null=True)
    invitation_created_at = models.DateTimeField(blank=True, null=True)
    invitation_sent_at = models.DateTimeField(blank=True, null=True)
    invitation_accepted_at = models.DateTimeField(blank=True, null=True)
    invitation_limit = models.IntegerField(blank=True, null=True)
    invited_by_type = models.CharField(max_length=255, blank=True, null=True)
    invited_by_id = models.BigIntegerField(blank=True, null=True)
    invitations_count = models.IntegerField(blank=True, null=True)
    preferred_language = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(unique=True, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    player = models.ForeignKey("Player", models.DO_NOTHING, blank=True, null=True, related_name='admin_user')
    sign_in_count = models.IntegerField(blank=True, null=True)
    current_sign_in_at = models.DateTimeField(blank=True, null=True)
    last_sign_in_at = models.DateTimeField(blank=True, null=True)
    current_sign_in_ip = models.GenericIPAddressField(blank=True, null=True)
    last_sign_in_ip = models.GenericIPAddressField(blank=True, null=True)
    otp_required_for_login = models.BooleanField(blank=True, null=True)
    otp_secret = models.CharField(max_length=255, blank=True, null=True)
    last_otp_timestep = models.IntegerField(blank=True, null=True)
    otp_backup_codes = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    preferences = models.JSONField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'users'


class Version(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_type = models.CharField(max_length=255, blank=True, null=True)
    item_id = models.BigIntegerField(blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    whodunnit = models.CharField(max_length=255, blank=True, null=True)
    object = models.TextField(blank=True, null=True)
    object_changes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'versions'
