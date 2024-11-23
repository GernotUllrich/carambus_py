from django.db import models


class AccountUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    account = models.ForeignKey('Account', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    roles = models.JSONField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'account_users'
        unique_together = (('account', 'user'),)
