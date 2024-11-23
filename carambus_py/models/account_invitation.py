from django.db import models


class AccountInvitation(models.Model):
    id = models.BigAutoField(primary_key=True)
    invited_by = models.ForeignKey('User',models.DO_NOTHING, blank=True, null=True, related_name='account_invitations_for_user')
    token = models.CharField(unique=True, blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    roles = models.JSONField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    account = models.ForeignKey('Account', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'account_invitations'
        unique_together = (('account', 'email'),)