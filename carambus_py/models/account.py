from django.db import models

class Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('carambus_py.User', models.DO_NOTHING, blank=True, null=True, related_name='accounts_for_owner')
    personal = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    account_users_count = models.IntegerField(default=0)  # Counter-Cache-Feld
    extra_billing_info = models.TextField(blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    subdomain = models.CharField(max_length=255, blank=True, null=True)
    billing_email = models.CharField(max_length=255, blank=True, null=True)
    users = models.ManyToManyField('carambus_py.User',
        through='AccountUser',
        related_name='accounts'  # Reverse accessor for User to Account
    )
    class Meta:
        db_table = 'accounts'