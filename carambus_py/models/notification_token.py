from django.db import models


class NotificationToken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField()
    platform = models.CharField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'notification_tokens'