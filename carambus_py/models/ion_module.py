from django.db import models

class IonModule(models.Model):
    id = models.BigAutoField(primary_key=True)
    module_id = models.CharField(max_length=255, blank=True, null=True)
    module_type = models.CharField(max_length=255, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    ion_content = models.ForeignKey('carambus_py.IonContent', on_delete=models.CASCADE, related_name='ion_modules_for_ion_content')

    class Meta:
        managed = True
        db_table = 'ion_modules'