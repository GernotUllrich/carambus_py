import sys

from .account import Account
from django.db import models
from django.db.models import F

class AccountUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    account = models.ForeignKey('carambus_py.Account', models.CASCADE, related_name='account_users', null=False, blank=False )
    user = models.ForeignKey('carambus_py.User', models.CASCADE, related_name='account_users', null=False, blank=False)
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