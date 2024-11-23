from django.db import models


class Plan(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    amount = models.IntegerField()
    interval = models.CharField()
    details = models.JSONField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    trial_period_days = models.IntegerField(blank=True, null=True)
    hidden = models.BooleanField(blank=True, null=True)
    currency = models.CharField(blank=True, null=True)
    interval_count = models.IntegerField(blank=True, null=True)
    description = models.CharField(blank=True, null=True)
    unit_label = models.CharField(blank=True, null=True)
    charge_per_unit = models.BooleanField(blank=True, null=True)
    stripe_id = models.CharField(blank=True, null=True)
    braintree_id = models.CharField(blank=True, null=True)
    paddle_billing_id = models.CharField(blank=True, null=True)
    paddle_classic_id = models.CharField(blank=True, null=True)
    lemon_squeezy_id = models.CharField(blank=True, null=True)
    fake_processor_id = models.CharField(blank=True, null=True)
    contact_url = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plans'