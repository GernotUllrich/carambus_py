from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class ConnectedAccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    owner_id = models.BigIntegerField(blank=True, null=True)
    provider = models.CharField(blank=True, null=True)
    uid = models.CharField(blank=True, null=True)
    refresh_token = models.CharField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    auth = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    access_token = models.CharField(blank=True, null=True)
    access_token_secret = models.CharField(blank=True, null=True)
    owner_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    owner = GenericForeignKey('owner_type', 'owner_id')

    class Meta:
        managed = False
        db_table = 'connected_accounts'