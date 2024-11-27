from bs4 import BeautifulSoup
import sys
import logging
import requests
from django.db import models
from typing import Optional
from carambus_py.models.region_cc_action import get_region_action_data


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from carambus_py.models import Branch, League, LeagueCc

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
    region = models.ForeignKey('carambus_py.Region', on_delete=models.CASCADE, related_name='region_ccs_for_region')

    # Set up logging
    REPORT_LOGGER = logging.getLogger("RegionCc")
    handler = None

    # Status mapping
    STATUS_MAP = {
        "active": 1,
        "passive": 2,
    }

    DEBUG = True

    # Class variable for mapping paths and read-only settings
    PATH_MAP = {
        "home": ["", True],
        "createLeagueSave": ["/admin/league/createLeagueSave.php", False],
        "showLeagueList": ["/admin/report/showLeagueList.php", True],
        "showLeague": ["/admin/league/showLeague.php", True],
        "admin_report_showLeague": ["/admin/report/showLeague.php", True],
        "admin_report_showLeague_create_team": ["/admin/report/showLeague_create_team.php", False],
        "spielbericht_anzeigen": ["/admin/reportbuilder2/spielbericht_anzeigen.php", True],
        "showTeam": ["/admin/announcement/team/showTeam.php", True],
        "editTeam": ["admin/announcement/team/editTeamCheck.php", False],
        "showClubList": ["/admin/announcement/team/showClubList.php", True],
        "showLeague_show_teamplayer": ["/admin/report/showLeague_show_teamplayer.php", True],
        "showLeague_add_teamplayer": ["/admin/report/showLeague_add_teamplayer.php", False],
        "showAnnounceList": ["/admin/announcement/team/showAnnounceList.php", True],
        "spielbericht": ["/admin/bm_mw/spielbericht.php", True],
        "showLeague_create_team_save": ["/admin/report/showLeague_create_team_save.php", False],
        "spielberichte": ["/admin/reportbuilder2/spielberichte.php", True],
        "spielberichtCheck": ["/admin/bm_mw/spielberichtCheck.php", True],
        "spielberichtSave": ["/admin/bm_mw/spielberichtSave.php", False],
        "massChangingCheck": ["/admin/report/massChangingCheck.php", True],
        "massChangingCheckAuth": ["/admin/report/massChangingCheckAuth.php", True],
        "showCategoryList": ["/admin/einzel/category/showCategoryList.php", True],
        "showCategory": ["/admin/einzel/category/showCategory.php", True],
        "editCategoryCheck": ["/admin/einzel/category/editCategoryCheck.php", True],
        "showTypeList": ["/admin/einzel/type/showTypeList.php", True],
        "showType": ["/admin/einzel/type/showType.php", True],
        "showSerienList": ["/admin/einzel/serie/showSerienList.php", True],
        "showSerie": ["/admin/einzel/serie/showSerie.php", True],
        "showGroupList": ["/admin/einzel/gruppen/showGroupList.php", True],
        "showGroup": ["/admin/einzel/gruppen/showGroup.php", True],
        "showMeldelistenList": ["/admin/einzel/meldelisten/showMeldelistenList.php", True],
        "showMeldeliste": ["/admin/einzel/meldelisten/showMeldeliste.php", True],
        "showMeisterschaftenList": ["/admin/einzel/meisterschaft/showMeisterschaftenList.php", True],
        "showMeisterschaft": ["/admin/einzel/meisterschaft/showMeisterschaft.php", True],
        "club-showMeldelistenList": ["/admin/einzel/clubmeldung/showMeldelistenList.php", True],
        "club-showMeldeliste": ["/admin/einzel/clubmeldung/showMeldeliste.php", True],
        "createMeldelisteSave": ["/admin/einzel/meldelisten/createMeldelisteSave.php", False],
        "createMeldelisteCheck": ["/admin/einzel/meldelisten/createMeldelisteCheck.php", False],
        "releaseMeldeliste": ["/admin/einzel/meldelisten/releaseMeldeliste.php", False],
        "createMeisterschaftSave": ["/admin/einzel/meisterschaft/createMeisterschaftSave.php", False],
        "editMeisterschaftCheck": ["/admin/einzel/meisterschaft/editMeisterschaftCheck.php", False],
        "editMeisterschaftSave": ["/admin/einzel/meisterschaft/editMeisterschaftSave.php", False],
        "deleteMeldeliste": ["/admin/einzel/meldelisten/deleteMeldeliste.php", False],
        "deleteErgebnis": ["/admin/einzel/meisterschaft/deleteErgebnis.php", False],
        "showErgebnisliste": ["/admin/einzel/meisterschaft/showErgebnisliste.php", False],
        "importErgebnisseStep1": ["/admin/einzel/meisterschaft/importErgebnisseStep1.php", False],
        "importErgebnisseStep2": ["/admin/einzel/meisterschaft/importErgebnisseStep2.php", False],
        "importErgebnisseStep3": ["/admin/einzel/meisterschaft/importErgebnisseStep3.php", False],
        "importRangliste1": ["/admin/einzel/meisterschaft/importRangliste1.php", False],
        "importRangliste2": ["/admin/einzel/meisterschaft/importRangliste2.php", False],
        "showRangliste": ["/admin/einzel/meisterschaft/showRangliste.php", False],
        "releaseRangliste.php": ["/admin/einzel/meisterschaft/releaseRangliste.php.php", False],
        "suche": ["suche.php", True],
    }

    # branch_ccs = rails_models.RelatedField('BranchCcs', related_name='regioncc')

    class Meta:
        managed = True
        db_table = 'region_ccs'
        unique_together = (('cc_id', 'context'),)
        if 'test' in sys.argv:
            managed = False
            unique_together = None

    @staticmethod
    def setup_logger(default_log="default.log"):
        # Initialize the logger if not already set up
        if RegionCc.handler is None:
            RegionCc.handler = logging.FileHandler(default_log)
            RegionCc.REPORT_LOGGER.addHandler(RegionCc.handler)
            RegionCc.REPORT_LOGGER.setLevel(logging.DEBUG)

    @staticmethod
    def save_log(name):
        if RegionCc.handler:
            RegionCc.handler.close()
            RegionCc.REPORT_LOGGER.removeHandler(RegionCc.handler)

        # Assign a new handler for the new log file
        RegionCc.handler = logging.FileHandler(f"{name}.log")
        RegionCc.REPORT_LOGGER.addHandler(RegionCc.handler)

    def sync_branches(self):
        """
        Synchronize branches by sending a POST request and processing the response.
        """
        url = f"{self.base_url}/some_endpoint"  # Update with the actual endpoint
        response = requests.post(url, data={"context": self.context})
        if response.status_code == 200:
            # Process response data
            data = response.json()
            for branch_data in data:
                # Assuming `Branch` is a model in Django
                branch, created = Branch.objects.update_or_create(
                    name=branch_data["name"],
                    defaults={
                        "context": self.context,
                        "some_field": branch_data["some_field"],
                    },
                )
                if created:
                    self.logger().info(f"Created branch: {branch.name}")
        else:
            self.logger().error(f"Failed to sync branches: {response.text}")

    def sync_leagues(self, opts=None):
        """
        Sync league data for a given season and context.
        """
        if opts is None:
            opts = {}

        season_name = opts.get("season_name")
        if not season_name:
            raise ValueError("Season name is required")

        leagues = League.objects.filter(season__name=season_name, context=self.context)
        for league in leagues:
            try:
                league_data = {
                    "name": league.name,
                    "context": self.context,
                    "shortname": league.shortname,
                }
                LeagueCc.objects.update_or_create(
                    league=league,
                    defaults=league_data,
                )
                self.logger().info(f"Synced league: {league.name}")
            except Exception as e:
                self.logger().error(f"Failed to sync league {league.name}: {str(e)}")

    @staticmethod
    def logger():
        # Placeholder logger
        import logging
        return logging.getLogger("RegionCc")

    @staticmethod
    def post_cc_with_formdata(action, post_options=None, opts=None):
        dry_run, opts, post_options, referer, region = RegionCc.prepare_for_post_cc(opts, post_options)

        if action in RegionCc.PATH_MAP:
            doc, read_only_action, res, url = RegionCc.post_cc_action(action, dry_run, post_options, region)

            if not dry_run or read_only_action:
                session = requests.Session()
                headers = {
                    "cookie": f"PHPSESSID={opts.get('session_id')}",
                    "referer": referer if referer else "",
                    "cache-control": "max-age=0",
                    "upgrade-insecure-requests": "1",
                    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                }

                # Clean empty values
                doc, res = RegionCc.response_for_post_cc(headers, post_options, session, url)

            return res, doc

    @staticmethod
    def post_cc(action, post_options=None, opts=None):
        dry_run, opts, post_options, referer, region = RegionCc.prepare_for_post_cc(opts, post_options)

        if action in RegionCc.PATH_MAP:
            doc, read_only_action, res, url = RegionCc.post_cc_action(action, dry_run, post_options, region)

            if not dry_run or read_only_action:
                session = requests.Session()
                headers = {
                    "cookie": f"PHPSESSID={opts.get('session_id')}",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "referer": referer if referer else "",
                    "cache-control": "max-age=0",
                    "upgrade-insecure-requests": "1",
                    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                }

                # Clean empty values
                doc, res = RegionCc.response_for_post_cc(headers, post_options, session, url)

            return res, doc

    @staticmethod
    def response_for_post_cc(headers, post_options, session, url):
        payload = {k: v for k, v in post_options.items() if v}
        response = session.post(url, headers=headers, data=payload)
        res = response
        if response.status_code == 200:
            doc = BeautifulSoup(response.text, "html.parser")
        else:
            doc = BeautifulSoup(response.reason, "html.parser")
        return doc, res

    @staticmethod
    def post_cc_action(action, dry_run, post_options, region):
        path, read_only_action = RegionCc.PATH_MAP[action]
        url = region.region_cc.base_url + path
        if read_only_action:
            if RegionCc.DEBUG:
                print(f"[{action}] POST {path} with payload {post_options}")
        else:
            RegionCc.logger().debug(
                f"[{action}] {'WILL' if dry_run else ''} POST {action} {path} with payload {post_options}"
            )
        res, doc = None, None
        return doc, read_only_action, res, url

    @staticmethod
    def prepare_for_post_cc(opts, post_options):
        if post_options is None:
            post_options = {}
        if opts is None:
            opts = {}
        dry_run = not opts.get("armed", False)
        # explicitly declares that referer can be either str or None.
        referer: Optional[str] = post_options.pop("referer", None)
        region = Region.objects.filter(shortname="NBV").first()
        referer = region.region_cc.base_url + referer if referer else None
        return dry_run, opts, post_options, referer, region