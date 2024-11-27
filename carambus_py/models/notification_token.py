from django.db import models

class NotificationToken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('carambus_py.User', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'notification_tokens'