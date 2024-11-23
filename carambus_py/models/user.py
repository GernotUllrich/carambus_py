from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True)
    encrypted_password = models.CharField()
    reset_password_token = models.CharField(unique=True, blank=True, null=True)
    reset_password_sent_at = models.DateTimeField(blank=True, null=True)
    remember_created_at = models.DateTimeField(blank=True, null=True)
    confirmation_token = models.CharField(unique=True, blank=True, null=True)
    confirmed_at = models.DateTimeField(blank=True, null=True)
    confirmation_sent_at = models.DateTimeField(blank=True, null=True)
    unconfirmed_email = models.CharField(blank=True, null=True)
    first_name = models.CharField(blank=True, null=True)
    last_name = models.CharField(blank=True, null=True)
    time_zone = models.CharField(blank=True, null=True)
    accepted_terms_at = models.DateTimeField(blank=True, null=True)
    accepted_privacy_at = models.DateTimeField(blank=True, null=True)
    announcements_read_at = models.DateTimeField(blank=True, null=True)
    admin = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    invitation_token = models.CharField(unique=True, blank=True, null=True)
    invitation_created_at = models.DateTimeField(blank=True, null=True)
    invitation_sent_at = models.DateTimeField(blank=True, null=True)
    invitation_accepted_at = models.DateTimeField(blank=True, null=True)
    invitation_limit = models.IntegerField(blank=True, null=True)
    invited_by_type = models.CharField(blank=True, null=True)
    invited_by_id = models.BigIntegerField(blank=True, null=True)
    invitations_count = models.IntegerField(blank=True, null=True)
    preferred_language = models.CharField(blank=True, null=True)
    username = models.CharField(unique=True, blank=True, null=True)
    firstname = models.CharField(blank=True, null=True)
    lastname = models.CharField(blank=True, null=True)
    player = models.ForeignKey("Player", models.DO_NOTHING, blank=True, null=True, related_name='users_for_player')
    sign_in_count = models.IntegerField(blank=True, null=True)
    current_sign_in_at = models.DateTimeField(blank=True, null=True)
    last_sign_in_at = models.DateTimeField(blank=True, null=True)
    current_sign_in_ip = models.GenericIPAddressField(blank=True, null=True)
    last_sign_in_ip = models.GenericIPAddressField(blank=True, null=True)
    otp_required_for_login = models.BooleanField(blank=True, null=True)
    otp_secret = models.CharField(blank=True, null=True)
    last_otp_timestep = models.IntegerField(blank=True, null=True)
    otp_backup_codes = models.TextField(blank=True, null=True)
    code = models.CharField(blank=True, null=True)
    preferences = models.JSONField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

    class Meta:
        db_table = 'users'