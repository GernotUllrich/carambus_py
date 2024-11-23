from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Addresse(models.Model):
    id = models.BigAutoField(primary_key=True)
    addressable_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Polymorphic type
    addressable_id = models.BigIntegerField()
    address_type = models.IntegerField(blank=True, null=True)
    line1 = models.CharField(blank=True, null=True)
    line2 = models.CharField(blank=True, null=True)
    city = models.CharField(blank=True, null=True)
    state = models.CharField(blank=True, null=True)
    country = models.CharField(blank=True, null=True)
    postal_code = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    addressable = GenericForeignKey('addressable_type', 'addressable_id')  # Combined polymorphic field

    class Meta:
        managed = False
        db_table = 'addresses'