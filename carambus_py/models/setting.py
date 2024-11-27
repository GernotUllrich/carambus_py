import yaml
import json
import requests
import hashlib

from django.core.exceptions import ObjectDoesNotExist
from django.db import models, transaction
from django.utils.timezone import now
from datetime import timedelta


from carambus_py.models.region_cc_action import RegionCcAction
from carambus_py.models.region import Region


class Setting(models.Model):
    data = models.TextField(default="{}", blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    region = models.ForeignKey('carambus_py.Region', on_delete=models.CASCADE, related_name='settings_for_region')
    club = models.ForeignKey('carambus_py.Club', on_delete=models.CASCADE, related_name='settings_for_club')
    tournament = models.ForeignKey('carambus_py.Tournament', on_delete=models.CASCADE, related_name='settings_for_tournament')

    SETTING = None  # Singleton instance placeholder
    MIN_ID = 50_000_000

    class Meta:
        managed = True
        db_table = 'settings'

    @classmethod
    def instance(cls):
        if cls.SETTING is None:
            cls.SETTING = cls.objects.first() or cls.objects.create()
        return cls.SETTING

    @classmethod
    def key_set_value(cls, key, value):
        try:
            with transaction.atomic():
                inst = cls.instance()
                # Deserialize YAML data into a dictionary
                try:
                    data = yaml.safe_load(inst.data) or {}
                except yaml.YAMLError:
                    data = {}
                # Update the dictionary
                if isinstance(value, (dict, list)):
                    serialized_value = yaml.dump(value)  # Convert to YAML string
                else:
                    serialized_value = str(value)
                data[key] = {"type": type(value).__name__, "value": serialized_value}

                # Serialize the updated dictionary back to YAML
                inst.data = yaml.dump(data)
                inst.save()

        except Exception as e:
            print(f"Error setting key value: {e}")
            return None

    @classmethod
    def key_get_value(cls, key):
        try:
            with transaction.atomic():
                inst = cls.instance()
                try:
                    data = yaml.safe_load(inst.data) or {}
                except yaml.YAMLError:
                    data = {}

                if key in data:
                    entry = data[key]
                    value_type = entry["type"]
                    value = entry["value"]

                    # Convert the value back to its original type
                    if value_type == "int":
                        return int(value)
                    elif value_type == "float":
                        return float(value)
                    elif value_type in ["dict", "list"]:
                        return yaml.safe_load(value)
                    return value
                return None
        except Exception as e:
            print(f"Error getting key value: {e}")
            return None

    @staticmethod
    def key_delete(k):
        try:
            with transaction.atomic():
                inst = Setting.objects.get()  # Assuming only one instance exists
                # Decode the YAML-encoded data
                hash_data = yaml.safe_load(inst.data) or {}

                # Remove the key if it exists
                hash_data.pop(str(k), None)

                # Mark the field as changed by re-encoding the YAML
                inst.data = yaml.dump(hash_data)

                # Save the changes
                inst.save(update_fields=["data"])
        except (ObjectDoesNotExist, Exception):
            return None


    @classmethod
    def login_to_cc(cls):
        from bs4 import BeautifulSoup

        opts = RegionCcAction.get_base_opts_from_environment()
        region = Region.objects.get(shortname=opts["context"].upper())
        region_cc = region.region_cc

        url = f"{region_cc.base_url}/index.php"
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        call_police = int(soup.find("input", {"name": "call_police"})["value"])
        userpw = region_cc.userpw
        md5pw = hashlib.md5(userpw.encode()).hexdigest()

        args = {
            "username": region_cc.username,
            "userpassword": md5pw,
            "call_police": call_police,
            "loginUser": region_cc.username,
            "userpw": userpw,
            "loginButton": "ANMELDEN",
        }
        response = region_cc.post_cc("checkUser", args, opts)
        session_id = BeautifulSoup(response[1], "html.parser").find("script").text.split("PHPSESSID=")[1].split("'")[0]
        cls.key_set_value("session_id", session_id)

    @classmethod
    def logoff_from_cc(cls):
        opts = RegionCcAction.get_base_opts_from_environment()
        region = Region.objects.get(shortname=opts["context"].upper())
        region_cc = region.region_cc
        region_cc.post_cc("logoff", {}, opts)
        cls.key_delete("session_id")

    @classmethod
    def get_carambus_api_token(cls):
        expire_str = cls.key_get_value("carambus_api_token_expire_at")
        if not expire_str or now() > expire_str:
            url = "https://dev-r4djmvaa.eu.auth0.com/oauth/token"
            payload = json.dumps({
                "client_id": "aqAJY7zNMsw0jiThccQyKOO1WyjKP0AC",
                "client_secret": "7PN4bsl0tikD8fylkoOY_j2RudtlayXVCI0SlPzG2Tfr7ewLUETiEYHFwVL9Rk1Q",
                "audience": "https://api.carambus.de",
                "grant_type": "client_credentials",
            })
            headers = {"Content-Type": "application/json"}

            response = requests.post(url, data=payload, headers=headers)
            if response.status_code != 200:
                return []

            resp_data = response.json()
            access_token = resp_data["access_token"]
            token_type = resp_data["token_type"]

            cls.key_set_value("carambus_api_access_token", access_token)
            cls.key_set_value("carambus_api_token_type", token_type)
            cls.key_set_value("carambus_api_token_expire_at", now() + timedelta(hours=10))  # 10 hours from now
        else:
            access_token = cls.key_get_value("carambus_api_access_token")
            token_type = cls.key_get_value("carambus_api_token_type")

        return access_token, token_type
