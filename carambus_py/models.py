# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange rails_models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the rails_models, but don't rename db_table values or field names.
from django.db import models


class ActionMailboxInboundEmail(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.IntegerField()
    message_id = models.CharField()
    message_checksum = models.CharField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'action_mailbox_inbound_emails'
        unique_together = (('message_id', 'message_checksum'),)


class ActionTextEmbed(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(blank=True, null=True)
    fields = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'action_text_embeds'


class ActionTextRichText(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    body = models.TextField(blank=True, null=True)
    record_type = models.CharField()
    record_id = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'action_text_rich_texts'
        unique_together = (('record_type', 'record_id', 'name'),)


class ActiveStorageAttachment(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    record_type = models.CharField()
    record_id = models.BigIntegerField()
    blob_id = models.BigIntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'active_storage_attachments'
        unique_together = (('record_type', 'record_id', 'name', 'blob_id'),)


class ActiveStorageBlob(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(unique=True)
    filename = models.CharField()
    content_type = models.CharField(blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)
    byte_size = models.BigIntegerField()
    checksum = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    service_name = models.CharField()

    class Meta:
        managed = False
        db_table = 'active_storage_blobs'


class ActiveStorageVariantRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    blob = models.ForeignKey(ActiveStorageBlob, models.DO_NOTHING)
    variation_digest = models.CharField()

    class Meta:
        managed = False
        db_table = 'active_storage_variant_records'
        unique_together = (('blob', 'variation_digest'),)


class ArInternalMetadata(models.Model):
    key = models.CharField(primary_key=True)
    value = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ar_internal_metadata'



class DjangoMigration(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class KvcSetting(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kvc_settings'



class NoticedEvent(models.Model):
    id = models.BigAutoField(primary_key=True)
    account_id = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(blank=True, null=True)
    record_type = models.CharField(blank=True, null=True)
    record_id = models.BigIntegerField(blank=True, null=True)
    params = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    notifications_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'noticed_events'


class NoticedNotification(models.Model):
    id = models.BigAutoField(primary_key=True)
    account_id = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(blank=True, null=True)
    event_id = models.BigIntegerField()
    recipient_type = models.CharField()
    recipient_id = models.BigIntegerField()
    read_at = models.DateTimeField(blank=True, null=True)
    seen_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'noticed_notifications'


class Notification(models.Model):
    id = models.BigAutoField(primary_key=True)
    account_id = models.BigIntegerField()
    recipient_type = models.CharField()
    recipient_id = models.BigIntegerField()
    type = models.CharField(blank=True, null=True)
    params = models.JSONField(blank=True, null=True)
    read_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    interacted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


class PayCharge(models.Model):
    id = models.BigAutoField(primary_key=True)
    processor_id = models.CharField()
    amount = models.IntegerField()
    amount_refunded = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    data = models.JSONField(blank=True, null=True)
    application_fee_amount = models.IntegerField(blank=True, null=True)
    currency = models.CharField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    subscription_id = models.IntegerField(blank=True, null=True)
    customer = models.ForeignKey('PayCustomer',models.DO_NOTHING, blank=True, null=True)
    stripe_account = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pay_charges'
        unique_together = (('customer', 'processor_id'),)


class PayCustomer(models.Model):
    id = models.BigAutoField(primary_key=True)
    owner_type = models.CharField(blank=True, null=True)
    owner_id = models.BigIntegerField(blank=True, null=True)
    processor = models.CharField(blank=True, null=True)
    processor_id = models.CharField(blank=True, null=True)
    default = models.BooleanField(blank=True, null=True)
    data = models.JSONField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    stripe_account = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pay_customers'


class PayMerchant(models.Model):
    id = models.BigAutoField(primary_key=True)
    owner_type = models.CharField(blank=True, null=True)
    owner_id = models.BigIntegerField(blank=True, null=True)
    processor = models.CharField(blank=True, null=True)
    processor_id = models.CharField(blank=True, null=True)
    default = models.BooleanField(blank=True, null=True)
    data = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pay_merchants'


class PayPaymentMethod(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(PayCustomer, models.DO_NOTHING, blank=True, null=True)
    processor_id = models.CharField(blank=True, null=True)
    default = models.BooleanField(blank=True, null=True)
    type = models.CharField(blank=True, null=True)
    data = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    stripe_account = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pay_payment_methods'
        unique_together = (('customer', 'processor_id'),)


class PaySubscription(models.Model):
    name = models.CharField()
    processor_id = models.CharField()
    processor_plan = models.CharField()
    quantity = models.IntegerField()
    trial_ends_at = models.DateTimeField(blank=True, null=True)
    ends_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(blank=True, null=True)
    data = models.JSONField(blank=True, null=True)
    application_fee_percent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    customer = models.ForeignKey(PayCustomer, models.DO_NOTHING, blank=True, null=True)
    current_period_start = models.DateTimeField(blank=True, null=True)
    current_period_end = models.DateTimeField(blank=True, null=True)
    metered = models.BooleanField(blank=True, null=True)
    pause_behavior = models.CharField(blank=True, null=True)
    pause_starts_at = models.DateTimeField(blank=True, null=True)
    pause_resumes_at = models.DateTimeField(blank=True, null=True)
    payment_method_id = models.CharField(blank=True, null=True)
    stripe_account = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pay_subscriptions'
        unique_together = (('customer', 'processor_id'),)


class PayWebhook(models.Model):
    id = models.BigAutoField(primary_key=True)
    processor = models.CharField(blank=True, null=True)
    event_type = models.CharField(blank=True, null=True)
    event = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pay_webhooks'
