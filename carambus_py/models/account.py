from django.db import models


class Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    owner = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True, related_name='accounts_for_owner')
    personal = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    extra_billing_info = models.TextField(blank=True, null=True)
    domain = models.CharField(blank=True, null=True)
    subdomain = models.CharField(blank=True, null=True)
    billing_email = models.CharField(blank=True, null=True)
    account_users_count = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'accounts'