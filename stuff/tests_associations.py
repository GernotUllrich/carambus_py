from django.test import TestCase

from django.db import IntegrityError


# Import all models_xxx
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from carambus_py.models_xxx import Account
from carambus_py.models_xxx import AccountInvitation
from carambus_py.models_xxx import AccountUser
from carambus_py.models_xxx import Addresse
from carambus_py.models_xxx import Announcement
from carambus_py.models_xxx import ApiToken
from carambus_py.models_xxx import BranchCc
from carambus_py.models_xxx import CalendarEvent
from carambus_py.models_xxx import CategoryCc
from carambus_py.models_xxx import ChampionshipTypeCc
from carambus_py.models_xxx import Club
from carambus_py.models_xxx import ClubLocation
from carambus_py.models_xxx import CompetitionCc
from carambus_py.models_xxx import ConnectedAccount
from carambus_py.models_xxx import Country
from carambus_py.models_xxx import DebugInfo
from carambus_py.models_xxx import Discipline
from carambus_py.models_xxx import DisciplineCc
from carambus_py.models_xxx import DisciplinePhase
from carambus_py.models_xxx import DisciplineTournamentPlan
from carambus_py.models_xxx import Game
from carambus_py.models_xxx import GameParticipation
from carambus_py.models_xxx import GamePlan
from carambus_py.models_xxx import GamePlanCc
from carambus_py.models_xxx import GamePlanRowCc
from carambus_py.models_xxx import GroupCc
from carambus_py.models_xxx import InboundWebhook
from carambus_py.models_xxx import IonContent
from carambus_py.models_xxx import IonModule
from carambus_py.models_xxx import League
from carambus_py.models_xxx import LeagueCc
from carambus_py.models_xxx import LeagueTeam
from carambus_py.models_xxx import LeagueTeamCc
from carambus_py.models_xxx import Location
from carambus_py.models_xxx import MetaMap
from carambus_py.models_xxx import NotificationToken
from carambus_py.models_xxx import Party
from carambus_py.models_xxx import PartyCc
from carambus_py.models_xxx import PartyGame
from carambus_py.models_xxx import PartyGameCc
from carambus_py.models_xxx import PartyMonitor
from carambus_py.models_xxx import Plan
from carambus_py.models_xxx import Player
from carambus_py.models_xxx import PlayerClass
from carambus_py.models_xxx import PlayerRanking
from carambus_py.models_xxx import Region
from carambus_py.models_xxx import RegionCc
from carambus_py.models_xxx import RegistrationCc
from carambus_py.models_xxx import RegistrationListCc
from carambus_py.models_xxx import Season
from carambus_py.models_xxx import SeasonCc
from carambus_py.models_xxx import SeasonParticipation
from carambus_py.models_xxx import Seeding
from carambus_py.models_xxx import Setting
from carambus_py.models_xxx import Slot
from carambus_py.models_xxx import SyncHash
from carambus_py.models_xxx import Table
from carambus_py.models_xxx import TableKind
from carambus_py.models_xxx import TableLocal
from carambus_py.models_xxx import TableMonitor
from carambus_py.models_xxx import Tournament
from carambus_py.models_xxx import TournamentCc
from carambus_py.models_xxx import TournamentLocal
from carambus_py.models_xxx import TournamentMonitor
from carambus_py.models_xxx import TournamentPlan
from carambus_py.models_xxx import TournamentSeriesCc
from carambus_py.models_xxx import Upload
from carambus_py.models_xxx import User
from carambus_py.models_xxx import Version


class AssociationTests(TestCase):

from carambus_py.models_xxx import LogEntry
    def test_logentry_user_foreign_key(self):
        """Test LogEntry.user ForeignKey to User"""
        try:
            obj = LogEntry.objects.create(user=User.objects.create())
            self.assertIsNotNone(obj.user)
        except IntegrityError:
            self.fail('LogEntry.user ForeignKey creation failed')


    def test_logentry_content_type_foreign_key(self):
        """Test LogEntry.content_type ForeignKey to ContentType"""
        try:
            obj = LogEntry.objects.create(content_type=ContentType.objects.create())
            self.assertIsNotNone(obj.content_type)
        except IntegrityError:
            self.fail('LogEntry.content_type ForeignKey creation failed')


from carambus_py.models_xxx import Permission
    def test_permission_content_type_foreign_key(self):
        """Test Permission.content_type ForeignKey to ContentType"""
        try:
            obj = Permission.objects.create(content_type=ContentType.objects.create())
            self.assertIsNotNone(obj.content_type)
        except IntegrityError:
            self.fail('Permission.content_type ForeignKey creation failed')


from carambus_py.models_xxx import Group
    def test_group_permissions_many_to_many_field(self):
        """Test Group.permissions ManyToManyField to Permission"""
        try:
            obj = Group.objects.create()
            related_obj = Permission.objects.create()
            obj.permissions.add(related_obj)
            self.assertIn(related_obj, obj.permissions.all())
        except IntegrityError:
            self.fail('Group.permissions ManyToManyField creation failed')


from carambus_py.models_xxx import User
    def test_user_groups_many_to_many_field(self):
        """Test User.groups ManyToManyField to Group"""
        try:
            obj = User.objects.create()
            related_obj = Group.objects.create()
            obj.groups.add(related_obj)
            self.assertIn(related_obj, obj.groups.all())
        except IntegrityError:
            self.fail('User.groups ManyToManyField creation failed')


    def test_user_user_permissions_many_to_many_field(self):
        """Test User.user_permissions ManyToManyField to Permission"""
        try:
            obj = User.objects.create()
            related_obj = Permission.objects.create()
            obj.user_permissions.add(related_obj)
            self.assertIn(related_obj, obj.user_permissions.all())
        except IntegrityError:
            self.fail('User.user_permissions ManyToManyField creation failed')


from carambus_py.models_xxx import ContentType
from carambus_py.models_xxx import Session
from carambus_py.models_xxx import Account
    def test_account_owner_foreign_key(self):
        """Test Account.owner ForeignKey to User"""
        try:
            obj = Account.objects.create(owner=User.objects.create())
            self.assertIsNotNone(obj.owner)
        except IntegrityError:
            self.fail('Account.owner ForeignKey creation failed')


from carambus_py.models_xxx import AccountInvitation
    def test_accountinvitation_invited_by_foreign_key(self):
        """Test AccountInvitation.invited_by ForeignKey to User"""
        try:
            obj = AccountInvitation.objects.create(invited_by=User.objects.create())
            self.assertIsNotNone(obj.invited_by)
        except IntegrityError:
            self.fail('AccountInvitation.invited_by ForeignKey creation failed')


    def test_accountinvitation_account_foreign_key(self):
        """Test AccountInvitation.account ForeignKey to Account"""
        try:
            obj = AccountInvitation.objects.create(account=Account.objects.create())
            self.assertIsNotNone(obj.account)
        except IntegrityError:
            self.fail('AccountInvitation.account ForeignKey creation failed')


from carambus_py.models_xxx import AccountUser
    def test_accountuser_account_foreign_key(self):
        """Test AccountUser.account ForeignKey to Account"""
        try:
            obj = AccountUser.objects.create(account=Account.objects.create())
            self.assertIsNotNone(obj.account)
        except IntegrityError:
            self.fail('AccountUser.account ForeignKey creation failed')


    def test_accountuser_user_foreign_key(self):
        """Test AccountUser.user ForeignKey to User"""
        try:
            obj = AccountUser.objects.create(user=User.objects.create())
            self.assertIsNotNone(obj.user)
        except IntegrityError:
            self.fail('AccountUser.user ForeignKey creation failed')


from carambus_py.models_xxx import Addresse
    def test_addresse_addressable_type_foreign_key(self):
        """Test Addresse.addressable_type ForeignKey to ContentType"""
        try:
            obj = Addresse.objects.create(addressable_type=ContentType.objects.create())
            self.assertIsNotNone(obj.addressable_type)
        except IntegrityError:
            self.fail('Addresse.addressable_type ForeignKey creation failed')


from carambus_py.models_xxx import Announcement
from carambus_py.models_xxx import ApiToken
    def test_apitoken_user_foreign_key(self):
        """Test ApiToken.user ForeignKey to User"""
        try:
            obj = ApiToken.objects.create(user=User.objects.create())
            self.assertIsNotNone(obj.user)
        except IntegrityError:
            self.fail('ApiToken.user ForeignKey creation failed')


from carambus_py.models_xxx import BranchCc
    def test_branchcc_discipline_foreign_key(self):
        """Test BranchCc.discipline ForeignKey to Discipline"""
        try:
            obj = BranchCc.objects.create(discipline=Discipline.objects.create())
            self.assertIsNotNone(obj.discipline)
        except IntegrityError:
            self.fail('BranchCc.discipline ForeignKey creation failed')


    def test_branchcc_region_cc_foreign_key(self):
        """Test BranchCc.region_cc ForeignKey to RegionCc"""
        try:
            obj = BranchCc.objects.create(region_cc=RegionCc.objects.create())
            self.assertIsNotNone(obj.region_cc)
        except IntegrityError:
            self.fail('BranchCc.region_cc ForeignKey creation failed')


from carambus_py.models_xxx import CalendarEvent
from carambus_py.models_xxx import CategoryCc
    def test_categorycc_branch_cc_foreign_key(self):
        """Test CategoryCc.branch_cc ForeignKey to BranchCc"""
        try:
            obj = CategoryCc.objects.create(branch_cc=BranchCc.objects.create())
            self.assertIsNotNone(obj.branch_cc)
        except IntegrityError:
            self.fail('CategoryCc.branch_cc ForeignKey creation failed')


from carambus_py.models_xxx import ChampionshipTypeCc
    def test_championshiptypecc_branch_cc_foreign_key(self):
        """Test ChampionshipTypeCc.branch_cc ForeignKey to BranchCc"""
        try:
            obj = ChampionshipTypeCc.objects.create(branch_cc=BranchCc.objects.create())
            self.assertIsNotNone(obj.branch_cc)
        except IntegrityError:
            self.fail('ChampionshipTypeCc.branch_cc ForeignKey creation failed')


from carambus_py.models_xxx import Club
    def test_club_region_foreign_key(self):
        """Test Club.region ForeignKey to Region"""
        try:
            obj = Club.objects.create(region=Region.objects.create())
            self.assertIsNotNone(obj.region)
        except IntegrityError:
            self.fail('Club.region ForeignKey creation failed')


from carambus_py.models_xxx import ClubLocation
    def test_clublocation_club_foreign_key(self):
        """Test ClubLocation.club ForeignKey to Club"""
        try:
            obj = ClubLocation.objects.create(club=Club.objects.create())
            self.assertIsNotNone(obj.club)
        except IntegrityError:
            self.fail('ClubLocation.club ForeignKey creation failed')


    def test_clublocation_location_foreign_key(self):
        """Test ClubLocation.location ForeignKey to Location"""
        try:
            obj = ClubLocation.objects.create(location=Location.objects.create())
            self.assertIsNotNone(obj.location)
        except IntegrityError:
            self.fail('ClubLocation.location ForeignKey creation failed')


from carambus_py.models_xxx import CompetitionCc
    def test_competitioncc_branch_cc_foreign_key(self):
        """Test CompetitionCc.branch_cc ForeignKey to BranchCc"""
        try:
            obj = CompetitionCc.objects.create(branch_cc=BranchCc.objects.create())
            self.assertIsNotNone(obj.branch_cc)
        except IntegrityError:
            self.fail('CompetitionCc.branch_cc ForeignKey creation failed')


    def test_competitioncc_discipline_foreign_key(self):
        """Test CompetitionCc.discipline ForeignKey to Discipline"""
        try:
            obj = CompetitionCc.objects.create(discipline=Discipline.objects.create())
            self.assertIsNotNone(obj.discipline)
        except IntegrityError:
            self.fail('CompetitionCc.discipline ForeignKey creation failed')


from carambus_py.models_xxx import ConnectedAccount
    def test_connectedaccount_owner_type_foreign_key(self):
        """Test ConnectedAccount.owner_type ForeignKey to ContentType"""
        try:
            obj = ConnectedAccount.objects.create(owner_type=ContentType.objects.create())
            self.assertIsNotNone(obj.owner_type)
        except IntegrityError:
            self.fail('ConnectedAccount.owner_type ForeignKey creation failed')


from carambus_py.models_xxx import Country
from carambus_py.models_xxx import DebugInfo
from carambus_py.models_xxx import Discipline
    def test_discipline_table_kind_foreign_key(self):
        """Test Discipline.table_kind ForeignKey to TableKind"""
        try:
            obj = Discipline.objects.create(table_kind=TableKind.objects.create())
            self.assertIsNotNone(obj.table_kind)
        except IntegrityError:
            self.fail('Discipline.table_kind ForeignKey creation failed')


    def test_discipline_super_discipline_foreign_key(self):
        """Test Discipline.super_discipline ForeignKey to Discipline"""
        try:
            obj = Discipline.objects.create(super_discipline=Discipline.objects.create())
            self.assertIsNotNone(obj.super_discipline)
        except IntegrityError:
            self.fail('Discipline.super_discipline ForeignKey creation failed')


    def test_discipline_discipline_cc_foreign_key(self):
        """Test Discipline.discipline_cc ForeignKey to DisciplineCc"""
        try:
            obj = Discipline.objects.create(discipline_cc=DisciplineCc.objects.create())
            self.assertIsNotNone(obj.discipline_cc)
        except IntegrityError:
            self.fail('Discipline.discipline_cc ForeignKey creation failed')


    def test_discipline_competition_cc_foreign_key(self):
        """Test Discipline.competition_cc ForeignKey to CompetitionCc"""
        try:
            obj = Discipline.objects.create(competition_cc=CompetitionCc.objects.create())
            self.assertIsNotNone(obj.competition_cc)
        except IntegrityError:
            self.fail('Discipline.competition_cc ForeignKey creation failed')


    def test_discipline_branch_cc_foreign_key(self):
        """Test Discipline.branch_cc ForeignKey to BranchCc"""
        try:
            obj = Discipline.objects.create(branch_cc=BranchCc.objects.create())
            self.assertIsNotNone(obj.branch_cc)
        except IntegrityError:
            self.fail('Discipline.branch_cc ForeignKey creation failed')


from carambus_py.models_xxx import DisciplineCc
    def test_disciplinecc_branch_cc_foreign_key(self):
        """Test DisciplineCc.branch_cc ForeignKey to BranchCc"""
        try:
            obj = DisciplineCc.objects.create(branch_cc=BranchCc.objects.create())
            self.assertIsNotNone(obj.branch_cc)
        except IntegrityError:
            self.fail('DisciplineCc.branch_cc ForeignKey creation failed')


    def test_disciplinecc_discipline_foreign_key(self):
        """Test DisciplineCc.discipline ForeignKey to Discipline"""
        try:
            obj = DisciplineCc.objects.create(discipline=Discipline.objects.create())
            self.assertIsNotNone(obj.discipline)
        except IntegrityError:
            self.fail('DisciplineCc.discipline ForeignKey creation failed')


from carambus_py.models_xxx import DisciplinePhase
from carambus_py.models_xxx import DisciplineTournamentPlan
    def test_disciplinetournamentplan_tournament_plan_foreign_key(self):
        """Test DisciplineTournamentPlan.tournament_plan ForeignKey to TournamentPlan"""
        try:
            obj = DisciplineTournamentPlan.objects.create(tournament_plan=TournamentPlan.objects.create())
            self.assertIsNotNone(obj.tournament_plan)
        except IntegrityError:
            self.fail('DisciplineTournamentPlan.tournament_plan ForeignKey creation failed')


    def test_disciplinetournamentplan_discipline_foreign_key(self):
        """Test DisciplineTournamentPlan.discipline ForeignKey to Discipline"""
        try:
            obj = DisciplineTournamentPlan.objects.create(discipline=Discipline.objects.create())
            self.assertIsNotNone(obj.discipline)
        except IntegrityError:
            self.fail('DisciplineTournamentPlan.discipline ForeignKey creation failed')


from carambus_py.models_xxx import Game
    def test_game_tournament_foreign_key(self):
        """Test Game.tournament ForeignKey to Tournament"""
        try:
            obj = Game.objects.create(tournament=Tournament.objects.create())
            self.assertIsNotNone(obj.tournament)
        except IntegrityError:
            self.fail('Game.tournament ForeignKey creation failed')


    def test_game_table_monitor_foreign_key(self):
        """Test Game.table_monitor ForeignKey to TableMonitor"""
        try:
            obj = Game.objects.create(table_monitor=TableMonitor.objects.create())
            self.assertIsNotNone(obj.table_monitor)
        except IntegrityError:
            self.fail('Game.table_monitor ForeignKey creation failed')


    def test_game_was_table_monitor_foreign_key(self):
        """Test Game.was_table_monitor ForeignKey to TableMonitor"""
        try:
            obj = Game.objects.create(was_table_monitor=TableMonitor.objects.create())
            self.assertIsNotNone(obj.was_table_monitor)
        except IntegrityError:
            self.fail('Game.was_table_monitor ForeignKey creation failed')


from carambus_py.models_xxx import GameParticipation
    def test_gameparticipation_player_foreign_key(self):
        """Test GameParticipation.player ForeignKey to Player"""
        try:
            obj = GameParticipation.objects.create(player=Player.objects.create())
            self.assertIsNotNone(obj.player)
        except IntegrityError:
            self.fail('GameParticipation.player ForeignKey creation failed')


    def test_gameparticipation_game_foreign_key(self):
        """Test GameParticipation.game ForeignKey to Game"""
        try:
            obj = GameParticipation.objects.create(game=Game.objects.create())
            self.assertIsNotNone(obj.game)
        except IntegrityError:
            self.fail('GameParticipation.game ForeignKey creation failed')


from carambus_py.models_xxx import GamePlan
from carambus_py.models_xxx import GamePlanCc
    def test_gameplancc_branch_cc_foreign_key(self):
        """Test GamePlanCc.branch_cc ForeignKey to BranchCc"""
        try:
            obj = GamePlanCc.objects.create(branch_cc=BranchCc.objects.create())
            self.assertIsNotNone(obj.branch_cc)
        except IntegrityError:
            self.fail('GamePlanCc.branch_cc ForeignKey creation failed')


    def test_gameplancc_discipline_foreign_key(self):
        """Test GamePlanCc.discipline ForeignKey to Discipline"""
        try:
            obj = GamePlanCc.objects.create(discipline=Discipline.objects.create())
            self.assertIsNotNone(obj.discipline)
        except IntegrityError:
            self.fail('GamePlanCc.discipline ForeignKey creation failed')


from carambus_py.models_xxx import GamePlanRowCc
    def test_gameplanrowcc_discipline_foreign_key(self):
        """Test GamePlanRowCc.discipline ForeignKey to Discipline"""
        try:
            obj = GamePlanRowCc.objects.create(discipline=Discipline.objects.create())
            self.assertIsNotNone(obj.discipline)
        except IntegrityError:
            self.fail('GamePlanRowCc.discipline ForeignKey creation failed')


from carambus_py.models_xxx import GroupCc
    def test_groupcc_branch_cc_foreign_key(self):
        """Test GroupCc.branch_cc ForeignKey to BranchCc"""
        try:
            obj = GroupCc.objects.create(branch_cc=BranchCc.objects.create())
            self.assertIsNotNone(obj.branch_cc)
        except IntegrityError:
            self.fail('GroupCc.branch_cc ForeignKey creation failed')


from carambus_py.models_xxx import InboundWebhook
from carambus_py.models_xxx import IonContent
from carambus_py.models_xxx import IonModule
    def test_ionmodule_ion_content_foreign_key(self):
        """Test IonModule.ion_content ForeignKey to IonContent"""
        try:
            obj = IonModule.objects.create(ion_content=IonContent.objects.create())
            self.assertIsNotNone(obj.ion_content)
        except IntegrityError:
            self.fail('IonModule.ion_content ForeignKey creation failed')


from carambus_py.models_xxx import League
    def test_league_organizer_type_foreign_key(self):
        """Test League.organizer_type ForeignKey to ContentType"""
        try:
            obj = League.objects.create(organizer_type=ContentType.objects.create())
            self.assertIsNotNone(obj.organizer_type)
        except IntegrityError:
            self.fail('League.organizer_type ForeignKey creation failed')


    def test_league_game_plan_foreign_key(self):
        """Test League.game_plan ForeignKey to GamePlan"""
        try:
            obj = League.objects.create(game_plan=GamePlan.objects.create())
            self.assertIsNotNone(obj.game_plan)
        except IntegrityError:
            self.fail('League.game_plan ForeignKey creation failed')


    def test_league_region_foreign_key(self):
        """Test League.region ForeignKey to Region"""
        try:
            obj = League.objects.create(region=Region.objects.create())
            self.assertIsNotNone(obj.region)
        except IntegrityError:
            self.fail('League.region ForeignKey creation failed')


    def test_league_discipline_foreign_key(self):
        """Test League.discipline ForeignKey to Discipline"""
        try:
            obj = League.objects.create(discipline=Discipline.objects.create())
            self.assertIsNotNone(obj.discipline)
        except IntegrityError:
            self.fail('League.discipline ForeignKey creation failed')


    def test_league_season_foreign_key(self):
        """Test League.season ForeignKey to Season"""
        try:
            obj = League.objects.create(season=Season.objects.create())
            self.assertIsNotNone(obj.season)
        except IntegrityError:
            self.fail('League.season ForeignKey creation failed')


    def test_league_league_cc_foreign_key(self):
        """Test League.league_cc ForeignKey to LeagueCc"""
        try:
            obj = League.objects.create(league_cc=LeagueCc.objects.create())
            self.assertIsNotNone(obj.league_cc)
        except IntegrityError:
            self.fail('League.league_cc ForeignKey creation failed')


from carambus_py.models_xxx import LeagueCc
    def test_leaguecc_season_cc_foreign_key(self):
        """Test LeagueCc.season_cc ForeignKey to SeasonCc"""
        try:
            obj = LeagueCc.objects.create(season_cc=SeasonCc.objects.create())
            self.assertIsNotNone(obj.season_cc)
        except IntegrityError:
            self.fail('LeagueCc.season_cc ForeignKey creation failed')


    def test_leaguecc_league_foreign_key(self):
        """Test LeagueCc.league ForeignKey to League"""
        try:
            obj = LeagueCc.objects.create(league=League.objects.create())
            self.assertIsNotNone(obj.league)
        except IntegrityError:
            self.fail('LeagueCc.league ForeignKey creation failed')


    def test_leaguecc_game_plan_cc_foreign_key(self):
        """Test LeagueCc.game_plan_cc ForeignKey to GamePlanCc"""
        try:
            obj = LeagueCc.objects.create(game_plan_cc=GamePlanCc.objects.create())
            self.assertIsNotNone(obj.game_plan_cc)
        except IntegrityError:
            self.fail('LeagueCc.game_plan_cc ForeignKey creation failed')


from carambus_py.models_xxx import LeagueTeam
    def test_leagueteam_league_foreign_key(self):
        """Test LeagueTeam.league ForeignKey to League"""
        try:
            obj = LeagueTeam.objects.create(league=League.objects.create())
            self.assertIsNotNone(obj.league)
        except IntegrityError:
            self.fail('LeagueTeam.league ForeignKey creation failed')


    def test_leagueteam_club_foreign_key(self):
        """Test LeagueTeam.club ForeignKey to Club"""
        try:
            obj = LeagueTeam.objects.create(club=Club.objects.create())
            self.assertIsNotNone(obj.club)
        except IntegrityError:
            self.fail('LeagueTeam.club ForeignKey creation failed')


    def test_leagueteam_league_team_cc_foreign_key(self):
        """Test LeagueTeam.league_team_cc ForeignKey to LeagueTeamCc"""
        try:
            obj = LeagueTeam.objects.create(league_team_cc=LeagueTeamCc.objects.create())
            self.assertIsNotNone(obj.league_team_cc)
        except IntegrityError:
            self.fail('LeagueTeam.league_team_cc ForeignKey creation failed')


from carambus_py.models_xxx import LeagueTeamCc
    def test_leagueteamcc_league_cc_foreign_key(self):
        """Test LeagueTeamCc.league_cc ForeignKey to LeagueCc"""
        try:
            obj = LeagueTeamCc.objects.create(league_cc=LeagueCc.objects.create())
            self.assertIsNotNone(obj.league_cc)
        except IntegrityError:
            self.fail('LeagueTeamCc.league_cc ForeignKey creation failed')


    def test_leagueteamcc_league_team_foreign_key(self):
        """Test LeagueTeamCc.league_team ForeignKey to LeagueTeam"""
        try:
            obj = LeagueTeamCc.objects.create(league_team=LeagueTeam.objects.create())
            self.assertIsNotNone(obj.league_team)
        except IntegrityError:
            self.fail('LeagueTeamCc.league_team ForeignKey creation failed')


from carambus_py.models_xxx import Location
    def test_location_organizer_type_foreign_key(self):
        """Test Location.organizer_type ForeignKey to ContentType"""
        try:
            obj = Location.objects.create(organizer_type=ContentType.objects.create())
            self.assertIsNotNone(obj.organizer_type)
        except IntegrityError:
            self.fail('Location.organizer_type ForeignKey creation failed')


    def test_location_club_foreign_key(self):
        """Test Location.club ForeignKey to Club"""
        try:
            obj = Location.objects.create(club=Club.objects.create())
            self.assertIsNotNone(obj.club)
        except IntegrityError:
            self.fail('Location.club ForeignKey creation failed')


    def test_location_region_foreign_key(self):
        """Test Location.region ForeignKey to Region"""
        try:
            obj = Location.objects.create(region=Region.objects.create())
            self.assertIsNotNone(obj.region)
        except IntegrityError:
            self.fail('Location.region ForeignKey creation failed')


from carambus_py.models_xxx import MetaMap
from carambus_py.models_xxx import NotificationToken
    def test_notificationtoken_user_foreign_key(self):
        """Test NotificationToken.user ForeignKey to User"""
        try:
            obj = NotificationToken.objects.create(user=User.objects.create())
            self.assertIsNotNone(obj.user)
        except IntegrityError:
            self.fail('NotificationToken.user ForeignKey creation failed')


from carambus_py.models_xxx import Party
    def test_party_league_foreign_key(self):
        """Test Party.league ForeignKey to League"""
        try:
            obj = Party.objects.create(league=League.objects.create())
            self.assertIsNotNone(obj.league)
        except IntegrityError:
            self.fail('Party.league ForeignKey creation failed')


    def test_party_league_team_a_foreign_key(self):
        """Test Party.league_team_a ForeignKey to LeagueTeam"""
        try:
            obj = Party.objects.create(league_team_a=LeagueTeam.objects.create())
            self.assertIsNotNone(obj.league_team_a)
        except IntegrityError:
            self.fail('Party.league_team_a ForeignKey creation failed')


    def test_party_league_team_b_foreign_key(self):
        """Test Party.league_team_b ForeignKey to LeagueTeam"""
        try:
            obj = Party.objects.create(league_team_b=LeagueTeam.objects.create())
            self.assertIsNotNone(obj.league_team_b)
        except IntegrityError:
            self.fail('Party.league_team_b ForeignKey creation failed')


    def test_party_host_league_team_foreign_key(self):
        """Test Party.host_league_team ForeignKey to LeagueTeam"""
        try:
            obj = Party.objects.create(host_league_team=LeagueTeam.objects.create())
            self.assertIsNotNone(obj.host_league_team)
        except IntegrityError:
            self.fail('Party.host_league_team ForeignKey creation failed')


    def test_party_location_foreign_key(self):
        """Test Party.location ForeignKey to Location"""
        try:
            obj = Party.objects.create(location=Location.objects.create())
            self.assertIsNotNone(obj.location)
        except IntegrityError:
            self.fail('Party.location ForeignKey creation failed')


    def test_party_no_show_team_foreign_key(self):
        """Test Party.no_show_team ForeignKey to LeagueTeam"""
        try:
            obj = Party.objects.create(no_show_team=LeagueTeam.objects.create())
            self.assertIsNotNone(obj.no_show_team)
        except IntegrityError:
            self.fail('Party.no_show_team ForeignKey creation failed')


    def test_party_party_monitor_foreign_key(self):
        """Test Party.party_monitor ForeignKey to PartyMonitor"""
        try:
            obj = Party.objects.create(party_monitor=PartyMonitor.objects.create())
            self.assertIsNotNone(obj.party_monitor)
        except IntegrityError:
            self.fail('Party.party_monitor ForeignKey creation failed')


    def test_party_party_cc_foreign_key(self):
        """Test Party.party_cc ForeignKey to PartyCc"""
        try:
            obj = Party.objects.create(party_cc=PartyCc.objects.create())
            self.assertIsNotNone(obj.party_cc)
        except IntegrityError:
            self.fail('Party.party_cc ForeignKey creation failed')


from carambus_py.models_xxx import PartyCc
    def test_partycc_league_cc_foreign_key(self):
        """Test PartyCc.league_cc ForeignKey to LeagueCc"""
        try:
            obj = PartyCc.objects.create(league_cc=LeagueCc.objects.create())
            self.assertIsNotNone(obj.league_cc)
        except IntegrityError:
            self.fail('PartyCc.league_cc ForeignKey creation failed')


    def test_partycc_league_team_a_cc_foreign_key(self):
        """Test PartyCc.league_team_a_cc ForeignKey to LeagueTeamCc"""
        try:
            obj = PartyCc.objects.create(league_team_a_cc=LeagueTeamCc.objects.create())
            self.assertIsNotNone(obj.league_team_a_cc)
        except IntegrityError:
            self.fail('PartyCc.league_team_a_cc ForeignKey creation failed')


    def test_partycc_league_team_b_cc_foreign_key(self):
        """Test PartyCc.league_team_b_cc ForeignKey to LeagueTeamCc"""
        try:
            obj = PartyCc.objects.create(league_team_b_cc=LeagueTeamCc.objects.create())
            self.assertIsNotNone(obj.league_team_b_cc)
        except IntegrityError:
            self.fail('PartyCc.league_team_b_cc ForeignKey creation failed')


    def test_partycc_league_team_host_cc_foreign_key(self):
        """Test PartyCc.league_team_host_cc ForeignKey to LeagueTeamCc"""
        try:
            obj = PartyCc.objects.create(league_team_host_cc=LeagueTeamCc.objects.create())
            self.assertIsNotNone(obj.league_team_host_cc)
        except IntegrityError:
            self.fail('PartyCc.league_team_host_cc ForeignKey creation failed')


    def test_partycc_party_foreign_key(self):
        """Test PartyCc.party ForeignKey to Party"""
        try:
            obj = PartyCc.objects.create(party=Party.objects.create())
            self.assertIsNotNone(obj.party)
        except IntegrityError:
            self.fail('PartyCc.party ForeignKey creation failed')


from carambus_py.models_xxx import PartyGame
    def test_partygame_party_foreign_key(self):
        """Test PartyGame.party ForeignKey to Party"""
        try:
            obj = PartyGame.objects.create(party=Party.objects.create())
            self.assertIsNotNone(obj.party)
        except IntegrityError:
            self.fail('PartyGame.party ForeignKey creation failed')


    def test_partygame_player_a_foreign_key(self):
        """Test PartyGame.player_a ForeignKey to Player"""
        try:
            obj = PartyGame.objects.create(player_a=Player.objects.create())
            self.assertIsNotNone(obj.player_a)
        except IntegrityError:
            self.fail('PartyGame.player_a ForeignKey creation failed')


    def test_partygame_player_b_foreign_key(self):
        """Test PartyGame.player_b ForeignKey to Player"""
        try:
            obj = PartyGame.objects.create(player_b=Player.objects.create())
            self.assertIsNotNone(obj.player_b)
        except IntegrityError:
            self.fail('PartyGame.player_b ForeignKey creation failed')


    def test_partygame_discipline_foreign_key(self):
        """Test PartyGame.discipline ForeignKey to Discipline"""
        try:
            obj = PartyGame.objects.create(discipline=Discipline.objects.create())
            self.assertIsNotNone(obj.discipline)
        except IntegrityError:
            self.fail('PartyGame.discipline ForeignKey creation failed')


    def test_partygame_party_game_cc_foreign_key(self):
        """Test PartyGame.party_game_cc ForeignKey to PartyGameCc"""
        try:
            obj = PartyGame.objects.create(party_game_cc=PartyGameCc.objects.create())
            self.assertIsNotNone(obj.party_game_cc)
        except IntegrityError:
            self.fail('PartyGame.party_game_cc ForeignKey creation failed')


from carambus_py.models_xxx import PartyGameCc
    def test_partygamecc_party_cc_foreign_key(self):
        """Test PartyGameCc.party_cc ForeignKey to PartyCc"""
        try:
            obj = PartyGameCc.objects.create(party_cc=PartyCc.objects.create())
            self.assertIsNotNone(obj.party_cc)
        except IntegrityError:
            self.fail('PartyGameCc.party_cc ForeignKey creation failed')


    def test_partygamecc_party_game_foreign_key(self):
        """Test PartyGameCc.party_game ForeignKey to PartyGame"""
        try:
            obj = PartyGameCc.objects.create(party_game=PartyGame.objects.create())
            self.assertIsNotNone(obj.party_game)
        except IntegrityError:
            self.fail('PartyGameCc.party_game ForeignKey creation failed')


from carambus_py.models_xxx import PartyMonitor
    def test_partymonitor_party_foreign_key(self):
        """Test PartyMonitor.party ForeignKey to Party"""
        try:
            obj = PartyMonitor.objects.create(party=Party.objects.create())
            self.assertIsNotNone(obj.party)
        except IntegrityError:
            self.fail('PartyMonitor.party ForeignKey creation failed')


from carambus_py.models_xxx import Plan
from carambus_py.models_xxx import Player
    def test_player_admin_user_foreign_key(self):
        """Test Player.admin_user ForeignKey to User"""
        try:
            obj = Player.objects.create(admin_user=User.objects.create())
            self.assertIsNotNone(obj.admin_user)
        except IntegrityError:
            self.fail('Player.admin_user ForeignKey creation failed')


from carambus_py.models_xxx import PlayerClass
    def test_playerclass_discipline_foreign_key(self):
        """Test PlayerClass.discipline ForeignKey to Discipline"""
        try:
            obj = PlayerClass.objects.create(discipline=Discipline.objects.create())
            self.assertIsNotNone(obj.discipline)
        except IntegrityError:
            self.fail('PlayerClass.discipline ForeignKey creation failed')


from carambus_py.models_xxx import PlayerRanking
    def test_playerranking_discipline_foreign_key(self):
        """Test PlayerRanking.discipline ForeignKey to Discipline"""
        try:
            obj = PlayerRanking.objects.create(discipline=Discipline.objects.create())
            self.assertIsNotNone(obj.discipline)
        except IntegrityError:
            self.fail('PlayerRanking.discipline ForeignKey creation failed')


    def test_playerranking_player_foreign_key(self):
        """Test PlayerRanking.player ForeignKey to Player"""
        try:
            obj = PlayerRanking.objects.create(player=Player.objects.create())
            self.assertIsNotNone(obj.player)
        except IntegrityError:
            self.fail('PlayerRanking.player ForeignKey creation failed')


    def test_playerranking_region_foreign_key(self):
        """Test PlayerRanking.region ForeignKey to Region"""
        try:
            obj = PlayerRanking.objects.create(region=Region.objects.create())
            self.assertIsNotNone(obj.region)
        except IntegrityError:
            self.fail('PlayerRanking.region ForeignKey creation failed')


    def test_playerranking_season_foreign_key(self):
        """Test PlayerRanking.season ForeignKey to Season"""
        try:
            obj = PlayerRanking.objects.create(season=Season.objects.create())
            self.assertIsNotNone(obj.season)
        except IntegrityError:
            self.fail('PlayerRanking.season ForeignKey creation failed')


    def test_playerranking_player_class_foreign_key(self):
        """Test PlayerRanking.player_class ForeignKey to PlayerClass"""
        try:
            obj = PlayerRanking.objects.create(player_class=PlayerClass.objects.create())
            self.assertIsNotNone(obj.player_class)
        except IntegrityError:
            self.fail('PlayerRanking.player_class ForeignKey creation failed')


    def test_playerranking_p_player_class_foreign_key(self):
        """Test PlayerRanking.p_player_class ForeignKey to PlayerClass"""
        try:
            obj = PlayerRanking.objects.create(p_player_class=PlayerClass.objects.create())
            self.assertIsNotNone(obj.p_player_class)
        except IntegrityError:
            self.fail('PlayerRanking.p_player_class ForeignKey creation failed')


    def test_playerranking_pp_player_class_foreign_key(self):
        """Test PlayerRanking.pp_player_class ForeignKey to PlayerClass"""
        try:
            obj = PlayerRanking.objects.create(pp_player_class=PlayerClass.objects.create())
            self.assertIsNotNone(obj.pp_player_class)
        except IntegrityError:
            self.fail('PlayerRanking.pp_player_class ForeignKey creation failed')


from carambus_py.models_xxx import Region
    def test_region_country_foreign_key(self):
        """Test Region.country ForeignKey to Country"""
        try:
            obj = Region.objects.create(country=Country.objects.create())
            self.assertIsNotNone(obj.country)
        except IntegrityError:
            self.fail('Region.country ForeignKey creation failed')


    def test_region_setting_foreign_key(self):
        """Test Region.setting ForeignKey to Setting"""
        try:
            obj = Region.objects.create(setting=Setting.objects.create())
            self.assertIsNotNone(obj.setting)
        except IntegrityError:
            self.fail('Region.setting ForeignKey creation failed')


    def test_region_region_cc_foreign_key(self):
        """Test Region.region_cc ForeignKey to RegionCc"""
        try:
            obj = Region.objects.create(region_cc=RegionCc.objects.create())
            self.assertIsNotNone(obj.region_cc)
        except IntegrityError:
            self.fail('Region.region_cc ForeignKey creation failed')


from carambus_py.models_xxx import RegionCc
    def test_regioncc_region_foreign_key(self):
        """Test RegionCc.region ForeignKey to Region"""
        try:
            obj = RegionCc.objects.create(region=Region.objects.create())
            self.assertIsNotNone(obj.region)
        except IntegrityError:
            self.fail('RegionCc.region ForeignKey creation failed')


from carambus_py.models_xxx import RegistrationCc
    def test_registrationcc_player_foreign_key(self):
        """Test RegistrationCc.player ForeignKey to Player"""
        try:
            obj = RegistrationCc.objects.create(player=Player.objects.create())
            self.assertIsNotNone(obj.player)
        except IntegrityError:
            self.fail('RegistrationCc.player ForeignKey creation failed')


    def test_registrationcc_registration_list_cc_foreign_key(self):
        """Test RegistrationCc.registration_list_cc ForeignKey to RegistrationListCc"""
        try:
            obj = RegistrationCc.objects.create(registration_list_cc=RegistrationListCc.objects.create())
            self.assertIsNotNone(obj.registration_list_cc)
        except IntegrityError:
            self.fail('RegistrationCc.registration_list_cc ForeignKey creation failed')


from carambus_py.models_xxx import RegistrationListCc
    def test_registrationlistcc_branch_cc_foreign_key(self):
        """Test RegistrationListCc.branch_cc ForeignKey to BranchCc"""
        try:
            obj = RegistrationListCc.objects.create(branch_cc=BranchCc.objects.create())
            self.assertIsNotNone(obj.branch_cc)
        except IntegrityError:
            self.fail('RegistrationListCc.branch_cc ForeignKey creation failed')


    def test_registrationlistcc_season_foreign_key(self):
        """Test RegistrationListCc.season ForeignKey to Season"""
        try:
            obj = RegistrationListCc.objects.create(season=Season.objects.create())
            self.assertIsNotNone(obj.season)
        except IntegrityError:
            self.fail('RegistrationListCc.season ForeignKey creation failed')


    def test_registrationlistcc_discipline_foreign_key(self):
        """Test RegistrationListCc.discipline ForeignKey to Discipline"""
        try:
            obj = RegistrationListCc.objects.create(discipline=Discipline.objects.create())
            self.assertIsNotNone(obj.discipline)
        except IntegrityError:
            self.fail('RegistrationListCc.discipline ForeignKey creation failed')


    def test_registrationlistcc_category_cc_foreign_key(self):
        """Test RegistrationListCc.category_cc ForeignKey to CategoryCc"""
        try:
            obj = RegistrationListCc.objects.create(category_cc=CategoryCc.objects.create())
            self.assertIsNotNone(obj.category_cc)
        except IntegrityError:
            self.fail('RegistrationListCc.category_cc ForeignKey creation failed')


from carambus_py.models_xxx import Season
from carambus_py.models_xxx import SeasonCc
    def test_seasoncc_competition_cc_foreign_key(self):
        """Test SeasonCc.competition_cc ForeignKey to CompetitionCc"""
        try:
            obj = SeasonCc.objects.create(competition_cc=CompetitionCc.objects.create())
            self.assertIsNotNone(obj.competition_cc)
        except IntegrityError:
            self.fail('SeasonCc.competition_cc ForeignKey creation failed')


    def test_seasoncc_season_foreign_key(self):
        """Test SeasonCc.season ForeignKey to Season"""
        try:
            obj = SeasonCc.objects.create(season=Season.objects.create())
            self.assertIsNotNone(obj.season)
        except IntegrityError:
            self.fail('SeasonCc.season ForeignKey creation failed')


from carambus_py.models_xxx import SeasonParticipation
    def test_seasonparticipation_season_foreign_key(self):
        """Test SeasonParticipation.season ForeignKey to Season"""
        try:
            obj = SeasonParticipation.objects.create(season=Season.objects.create())
            self.assertIsNotNone(obj.season)
        except IntegrityError:
            self.fail('SeasonParticipation.season ForeignKey creation failed')


    def test_seasonparticipation_player_foreign_key(self):
        """Test SeasonParticipation.player ForeignKey to Player"""
        try:
            obj = SeasonParticipation.objects.create(player=Player.objects.create())
            self.assertIsNotNone(obj.player)
        except IntegrityError:
            self.fail('SeasonParticipation.player ForeignKey creation failed')


    def test_seasonparticipation_club_foreign_key(self):
        """Test SeasonParticipation.club ForeignKey to Club"""
        try:
            obj = SeasonParticipation.objects.create(club=Club.objects.create())
            self.assertIsNotNone(obj.club)
        except IntegrityError:
            self.fail('SeasonParticipation.club ForeignKey creation failed')


from carambus_py.models_xxx import Seeding
    def test_seeding_player_foreign_key(self):
        """Test Seeding.player ForeignKey to Player"""
        try:
            obj = Seeding.objects.create(player=Player.objects.create())
            self.assertIsNotNone(obj.player)
        except IntegrityError:
            self.fail('Seeding.player ForeignKey creation failed')


    def test_seeding_playing_discipline_foreign_key(self):
        """Test Seeding.playing_discipline ForeignKey to Discipline"""
        try:
            obj = Seeding.objects.create(playing_discipline=Discipline.objects.create())
            self.assertIsNotNone(obj.playing_discipline)
        except IntegrityError:
            self.fail('Seeding.playing_discipline ForeignKey creation failed')


    def test_seeding_league_team_foreign_key(self):
        """Test Seeding.league_team ForeignKey to LeagueTeam"""
        try:
            obj = Seeding.objects.create(league_team=LeagueTeam.objects.create())
            self.assertIsNotNone(obj.league_team)
        except IntegrityError:
            self.fail('Seeding.league_team ForeignKey creation failed')


    def test_seeding_tournament_type_foreign_key(self):
        """Test Seeding.tournament_type ForeignKey to ContentType"""
        try:
            obj = Seeding.objects.create(tournament_type=ContentType.objects.create())
            self.assertIsNotNone(obj.tournament_type)
        except IntegrityError:
            self.fail('Seeding.tournament_type ForeignKey creation failed')


from carambus_py.models_xxx import Setting
    def test_setting_region_foreign_key(self):
        """Test Setting.region ForeignKey to Region"""
        try:
            obj = Setting.objects.create(region=Region.objects.create())
            self.assertIsNotNone(obj.region)
        except IntegrityError:
            self.fail('Setting.region ForeignKey creation failed')


    def test_setting_club_foreign_key(self):
        """Test Setting.club ForeignKey to Club"""
        try:
            obj = Setting.objects.create(club=Club.objects.create())
            self.assertIsNotNone(obj.club)
        except IntegrityError:
            self.fail('Setting.club ForeignKey creation failed')


    def test_setting_tournament_foreign_key(self):
        """Test Setting.tournament ForeignKey to Tournament"""
        try:
            obj = Setting.objects.create(tournament=Tournament.objects.create())
            self.assertIsNotNone(obj.tournament)
        except IntegrityError:
            self.fail('Setting.tournament ForeignKey creation failed')


from carambus_py.models_xxx import Slot
from carambus_py.models_xxx import SyncHash
from carambus_py.models_xxx import Table
    def test_table_location_foreign_key(self):
        """Test Table.location ForeignKey to Location"""
        try:
            obj = Table.objects.create(location=Location.objects.create())
            self.assertIsNotNone(obj.location)
        except IntegrityError:
            self.fail('Table.location ForeignKey creation failed')


    def test_table_table_kind_foreign_key(self):
        """Test Table.table_kind ForeignKey to TableKind"""
        try:
            obj = Table.objects.create(table_kind=TableKind.objects.create())
            self.assertIsNotNone(obj.table_kind)
        except IntegrityError:
            self.fail('Table.table_kind ForeignKey creation failed')


    def test_table_table_monitor_foreign_key(self):
        """Test Table.table_monitor ForeignKey to TableMonitor"""
        try:
            obj = Table.objects.create(table_monitor=TableMonitor.objects.create())
            self.assertIsNotNone(obj.table_monitor)
        except IntegrityError:
            self.fail('Table.table_monitor ForeignKey creation failed')


    def test_table_table_local_foreign_key(self):
        """Test Table.table_local ForeignKey to TableLocal"""
        try:
            obj = Table.objects.create(table_local=TableLocal.objects.create())
            self.assertIsNotNone(obj.table_local)
        except IntegrityError:
            self.fail('Table.table_local ForeignKey creation failed')


from carambus_py.models_xxx import TableKind
from carambus_py.models_xxx import TableLocal
    def test_tablelocal_table_foreign_key(self):
        """Test TableLocal.table ForeignKey to Table"""
        try:
            obj = TableLocal.objects.create(table=Table.objects.create())
            self.assertIsNotNone(obj.table)
        except IntegrityError:
            self.fail('TableLocal.table ForeignKey creation failed')


from carambus_py.models_xxx import TableMonitor
    def test_tablemonitor_prev_tournament_monitor_type_foreign_key(self):
        """Test TableMonitor.prev_tournament_monitor_type ForeignKey to ContentType"""
        try:
            obj = TableMonitor.objects.create(prev_tournament_monitor_type=ContentType.objects.create())
            self.assertIsNotNone(obj.prev_tournament_monitor_type)
        except IntegrityError:
            self.fail('TableMonitor.prev_tournament_monitor_type ForeignKey creation failed')


    def test_tablemonitor_tournament_monitor_foreign_key(self):
        """Test TableMonitor.tournament_monitor ForeignKey to TournamentMonitor"""
        try:
            obj = TableMonitor.objects.create(tournament_monitor=TournamentMonitor.objects.create())
            self.assertIsNotNone(obj.tournament_monitor)
        except IntegrityError:
            self.fail('TableMonitor.tournament_monitor ForeignKey creation failed')


    def test_tablemonitor_game_foreign_key(self):
        """Test TableMonitor.game ForeignKey to Game"""
        try:
            obj = TableMonitor.objects.create(game=Game.objects.create())
            self.assertIsNotNone(obj.game)
        except IntegrityError:
            self.fail('TableMonitor.game ForeignKey creation failed')


    def test_tablemonitor_prev_game_foreign_key(self):
        """Test TableMonitor.prev_game ForeignKey to Game"""
        try:
            obj = TableMonitor.objects.create(prev_game=Game.objects.create())
            self.assertIsNotNone(obj.prev_game)
        except IntegrityError:
            self.fail('TableMonitor.prev_game ForeignKey creation failed')


    def test_tablemonitor_table_foreign_key(self):
        """Test TableMonitor.table ForeignKey to Table"""
        try:
            obj = TableMonitor.objects.create(table=Table.objects.create())
            self.assertIsNotNone(obj.table)
        except IntegrityError:
            self.fail('TableMonitor.table ForeignKey creation failed')


from carambus_py.models_xxx import Tournament
    def test_tournament_organizer_type_foreign_key(self):
        """Test Tournament.organizer_type ForeignKey to ContentType"""
        try:
            obj = Tournament.objects.create(organizer_type=ContentType.objects.create())
            self.assertIsNotNone(obj.organizer_type)
        except IntegrityError:
            self.fail('Tournament.organizer_type ForeignKey creation failed')


    def test_tournament_discipline_foreign_key(self):
        """Test Tournament.discipline ForeignKey to Discipline"""
        try:
            obj = Tournament.objects.create(discipline=Discipline.objects.create())
            self.assertIsNotNone(obj.discipline)
        except IntegrityError:
            self.fail('Tournament.discipline ForeignKey creation failed')


    def test_tournament_region_foreign_key(self):
        """Test Tournament.region ForeignKey to Region"""
        try:
            obj = Tournament.objects.create(region=Region.objects.create())
            self.assertIsNotNone(obj.region)
        except IntegrityError:
            self.fail('Tournament.region ForeignKey creation failed')


    def test_tournament_season_foreign_key(self):
        """Test Tournament.season ForeignKey to Season"""
        try:
            obj = Tournament.objects.create(season=Season.objects.create())
            self.assertIsNotNone(obj.season)
        except IntegrityError:
            self.fail('Tournament.season ForeignKey creation failed')


    def test_tournament_tournament_plan_foreign_key(self):
        """Test Tournament.tournament_plan ForeignKey to TournamentPlan"""
        try:
            obj = Tournament.objects.create(tournament_plan=TournamentPlan.objects.create())
            self.assertIsNotNone(obj.tournament_plan)
        except IntegrityError:
            self.fail('Tournament.tournament_plan ForeignKey creation failed')


    def test_tournament_league_foreign_key(self):
        """Test Tournament.league ForeignKey to League"""
        try:
            obj = Tournament.objects.create(league=League.objects.create())
            self.assertIsNotNone(obj.league)
        except IntegrityError:
            self.fail('Tournament.league ForeignKey creation failed')


    def test_tournament_tournament_monitor_foreign_key(self):
        """Test Tournament.tournament_monitor ForeignKey to TournamentMonitor"""
        try:
            obj = Tournament.objects.create(tournament_monitor=TournamentMonitor.objects.create())
            self.assertIsNotNone(obj.tournament_monitor)
        except IntegrityError:
            self.fail('Tournament.tournament_monitor ForeignKey creation failed')


    def test_tournament_tournament_cc_foreign_key(self):
        """Test Tournament.tournament_cc ForeignKey to TournamentCc"""
        try:
            obj = Tournament.objects.create(tournament_cc=TournamentCc.objects.create())
            self.assertIsNotNone(obj.tournament_cc)
        except IntegrityError:
            self.fail('Tournament.tournament_cc ForeignKey creation failed')


    def test_tournament_setting_foreign_key(self):
        """Test Tournament.setting ForeignKey to Setting"""
        try:
            obj = Tournament.objects.create(setting=Setting.objects.create())
            self.assertIsNotNone(obj.setting)
        except IntegrityError:
            self.fail('Tournament.setting ForeignKey creation failed')


    def test_tournament_location_foreign_key(self):
        """Test Tournament.location ForeignKey to Location"""
        try:
            obj = Tournament.objects.create(location=Location.objects.create())
            self.assertIsNotNone(obj.location)
        except IntegrityError:
            self.fail('Tournament.location ForeignKey creation failed')


    def test_tournament_tournament_local_foreign_key(self):
        """Test Tournament.tournament_local ForeignKey to TournamentLocal"""
        try:
            obj = Tournament.objects.create(tournament_local=TournamentLocal.objects.create())
            self.assertIsNotNone(obj.tournament_local)
        except IntegrityError:
            self.fail('Tournament.tournament_local ForeignKey creation failed')


from carambus_py.models_xxx import TournamentCc
    def test_tournamentcc_branch_cc_foreign_key(self):
        """Test TournamentCc.branch_cc ForeignKey to BranchCc"""
        try:
            obj = TournamentCc.objects.create(branch_cc=BranchCc.objects.create())
            self.assertIsNotNone(obj.branch_cc)
        except IntegrityError:
            self.fail('TournamentCc.branch_cc ForeignKey creation failed')


    def test_tournamentcc_location_foreign_key(self):
        """Test TournamentCc.location ForeignKey to Location"""
        try:
            obj = TournamentCc.objects.create(location=Location.objects.create())
            self.assertIsNotNone(obj.location)
        except IntegrityError:
            self.fail('TournamentCc.location ForeignKey creation failed')


    def test_tournamentcc_registration_list_cc_foreign_key(self):
        """Test TournamentCc.registration_list_cc ForeignKey to RegistrationListCc"""
        try:
            obj = TournamentCc.objects.create(registration_list_cc=RegistrationListCc.objects.create())
            self.assertIsNotNone(obj.registration_list_cc)
        except IntegrityError:
            self.fail('TournamentCc.registration_list_cc ForeignKey creation failed')


    def test_tournamentcc_discipline_foreign_key(self):
        """Test TournamentCc.discipline ForeignKey to Discipline"""
        try:
            obj = TournamentCc.objects.create(discipline=Discipline.objects.create())
            self.assertIsNotNone(obj.discipline)
        except IntegrityError:
            self.fail('TournamentCc.discipline ForeignKey creation failed')


    def test_tournamentcc_group_cc_foreign_key(self):
        """Test TournamentCc.group_cc ForeignKey to GroupCc"""
        try:
            obj = TournamentCc.objects.create(group_cc=GroupCc.objects.create())
            self.assertIsNotNone(obj.group_cc)
        except IntegrityError:
            self.fail('TournamentCc.group_cc ForeignKey creation failed')


    def test_tournamentcc_championship_type_cc_foreign_key(self):
        """Test TournamentCc.championship_type_cc ForeignKey to ChampionshipTypeCc"""
        try:
            obj = TournamentCc.objects.create(championship_type_cc=ChampionshipTypeCc.objects.create())
            self.assertIsNotNone(obj.championship_type_cc)
        except IntegrityError:
            self.fail('TournamentCc.championship_type_cc ForeignKey creation failed')


    def test_tournamentcc_category_cc_foreign_key(self):
        """Test TournamentCc.category_cc ForeignKey to CategoryCc"""
        try:
            obj = TournamentCc.objects.create(category_cc=CategoryCc.objects.create())
            self.assertIsNotNone(obj.category_cc)
        except IntegrityError:
            self.fail('TournamentCc.category_cc ForeignKey creation failed')


    def test_tournamentcc_tournament_series_cc_foreign_key(self):
        """Test TournamentCc.tournament_series_cc ForeignKey to TournamentSeriesCc"""
        try:
            obj = TournamentCc.objects.create(tournament_series_cc=TournamentSeriesCc.objects.create())
            self.assertIsNotNone(obj.tournament_series_cc)
        except IntegrityError:
            self.fail('TournamentCc.tournament_series_cc ForeignKey creation failed')


    def test_tournamentcc_tournament_foreign_key(self):
        """Test TournamentCc.tournament ForeignKey to Tournament"""
        try:
            obj = TournamentCc.objects.create(tournament=Tournament.objects.create())
            self.assertIsNotNone(obj.tournament)
        except IntegrityError:
            self.fail('TournamentCc.tournament ForeignKey creation failed')


from carambus_py.models_xxx import TournamentLocal
    def test_tournamentlocal_tournament_foreign_key(self):
        """Test TournamentLocal.tournament ForeignKey to Tournament"""
        try:
            obj = TournamentLocal.objects.create(tournament=Tournament.objects.create())
            self.assertIsNotNone(obj.tournament)
        except IntegrityError:
            self.fail('TournamentLocal.tournament ForeignKey creation failed')


from carambus_py.models_xxx import TournamentMonitor
    def test_tournamentmonitor_tournament_foreign_key(self):
        """Test TournamentMonitor.tournament ForeignKey to Tournament"""
        try:
            obj = TournamentMonitor.objects.create(tournament=Tournament.objects.create())
            self.assertIsNotNone(obj.tournament)
        except IntegrityError:
            self.fail('TournamentMonitor.tournament ForeignKey creation failed')


from carambus_py.models_xxx import TournamentPlan
from carambus_py.models_xxx import TournamentSeriesCc
from carambus_py.models_xxx import Upload
from carambus_py.models_xxx import User
    def test_user_player_foreign_key(self):
        """Test User.player ForeignKey to Player"""
        try:
            obj = User.objects.create(player=Player.objects.create())
            self.assertIsNotNone(obj.player)
        except IntegrityError:
            self.fail('User.player ForeignKey creation failed')


from carambus_py.models_xxx import Version