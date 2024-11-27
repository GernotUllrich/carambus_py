from django.db import models

class InboundWebhook(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.IntegerField()
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'inbound_webhooks'