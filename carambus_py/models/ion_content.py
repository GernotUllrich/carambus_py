from django.db import models

class IonContent(models.Model):
    id = models.BigAutoField(primary_key=True)
    page_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    level = models.CharField(max_length=255, blank=True, null=True)
    scraped_at = models.DateTimeField(blank=True, null=True)
    deep_scraped_at = models.DateTimeField(blank=True, null=True)
    ion_content_id = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.BooleanField()

    # ion_modules = rails_models.RelatedField('IonModules', related_name='ioncontent')

    class Meta:
        managed = True
        db_table = 'ion_contents'