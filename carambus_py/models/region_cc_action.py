import os
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
import logging
from carambus_py.models import Setting, League, Region, RegionCc, Branch
from carambus_py.models import TournamentCc, BranchCc, CompetitionCc, GamePlanRowCc, LeagueCc, GamePlanCc, LeagueTeamCc, PartyCc, PartyGameCc, SeasonCc, ChampionshipTypeCc, CategoryCc, GroupCc, RegistrationListCc, RegistrationCc

logger = logging.getLogger(__name__)

class RegionCcAction:
    @staticmethod
    def get_base_opts_from_environment():
        session_id = os.getenv("PHPSESSID") or Setting.key_get_value("session_id")
        context = (
            os.getenv("CC_REGION", "").upper() or
            Setting.key_get_value("context") or
            "NBV"
        ).lower()
        season_name = os.getenv("CC_SEASON") or Setting.key_get_value("season_name")
        force_update = (
            os.getenv("CC_UPDATE", "").lower() == "true" or
            Setting.key_get_value("force_update") == "true"
        )

        exclude_season_names = [
            "2009/2010", "2010/2011", "2011/2012", "2012/2013",
            "2013/2014", "2014/2015", "2015/2016", "2016/2017",
            "2017/2018", "2018/2019", "2019/2020", "2020/2021",
            "2021/2022"
        ]

        pool_ba_ids = list(
            League.objects.filter(
                Q(organizer_id__in=[1, 17]) &
                Q(discipline__name__icontains="Pool")
            ).values_list("ba_id", flat=True)
        )

        snooker_ba_ids = list(
            League.objects.filter(
                Q(organizer_id__in=[1, 17]) &
                Q(discipline__name__icontains="Snooker")
            ).values_list("ba_id", flat=True)
        )

        karambol_ba_ids = list(
            League.objects.filter(
                Q(organizer_id__in=[1, 17]) &
                Q(discipline__name__icontains="Karambol")
            ).exclude(name__icontains="NDMM Dreiband MB")
            .values_list("ba_id", flat=True)
        )

        exclude_league_ba_ids = pool_ba_ids + snooker_ba_ids + karambol_ba_ids

        pool_ba_ids = list(
            TournamentCc.objects.filter(
                Q(tournament__organizer_id__in=[1, 17]) &
                Q(branch_cc__name__icontains="Pool") &
                Q(season__in=exclude_season_names)
            ).values_list("tournament__ba_id", flat=True)
        )

        snooker_ba_ids = list(
            TournamentCc.objects.filter(
                Q(tournament__organizer_id__in=[1, 17]) &
                Q(branch_cc__name__icontains="Snooker") &
                Q(season__in=exclude_season_names)
            ).values_list("tournament__ba_id", flat=True)
        )

        karambol_ba_ids = list(
            TournamentCc.objects.filter(
                Q(tournament__organizer_id__in=[1, 17]) &
                Q(branch_cc__name__icontains="Karambol") &
                Q(season__in=exclude_season_names)
            ).values_list("tournament__ba_id", flat=True)
        )

        exclude_tournament_ba_ids = pool_ba_ids + snooker_ba_ids + karambol_ba_ids

        return {
            "session_id": session_id,
            "armed": force_update,
            "context": context,
            "season_name": season_name,
            "exclude_season_names": exclude_season_names,
            "exclude_league_ba_ids": exclude_league_ba_ids,
            "exclude_tournament_ba_ids": exclude_tournament_ba_ids,
        }

    @staticmethod
    def remove_local_objects(opts):
        if opts.get("armed", False):
            models_to_clear = [
                RegionCc, BranchCc, CompetitionCc, GamePlanCc, GamePlanRowCc,
                LeagueCc, LeagueTeamCc, PartyCc, PartyGameCc, SeasonCc,
                ChampionshipTypeCc, CategoryCc, GroupCc, RegistrationListCc,
                RegistrationCc, TournamentCc
            ]
            for model in models_to_clear:
                model.objects.filter(id__gt=50000000).delete()
        else:
            logger.info("REPORT WARNING: Objects will be deleted (Preview Mode)")

    @staticmethod
    def synchronize_region_structure(opts):
        context = opts.get("context")
        try:
            region = Region.objects.get(shortname=context.upper())
        except ObjectDoesNotExist:
            raise ValueError(f"Unknown context Region {context}")

        regions_todo = [region.id]
        regions_done = RegionCc.sync_regions(opts)
        regions_still_todo = set(regions_todo) - set(regions_done)

        if regions_still_todo:
            raise ValueError(f"Regions with context {context} not yet in CC.")

    @staticmethod
    def synchronize_branch_structure(opts):
        context = os.getenv("REGION", "NBV").lower()
        try:
            region = Region.objects.get(shortname=context.upper())
        except ObjectDoesNotExist:
            raise ValueError(f"Unknown context Region {context}")

        branches_todo = list(Branch.objects.values_list("id", flat=True))
        branches_done = region.region_cc.sync_branches(opts)
        branches_still_todo = set(branches_todo) - set(branches_done)

        if branches_still_todo:
            raise ValueError(f"Branches not yet in CC: {branches_still_todo}")

    @staticmethod
    def raise_err_msg(context, msg):
        logger.error(f"[{context}] {msg}")
        raise ValueError(msg)
