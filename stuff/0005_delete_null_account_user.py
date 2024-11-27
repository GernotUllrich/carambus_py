from django.db import migrations

def delete_null_user_or_account(apps, schema_editor):
    AccountUser = apps.get_model("carambus_py", "AccountUser")
    # Delete records where user or account is NULL
    AccountUser.objects.filter(user__isnull=True).delete()
    AccountUser.objects.filter(account__isnull=True).delete()

class Migration(migrations.Migration):
    dependencies = [
        ("carambus_py", "0004_alter_account_billing_email_alter_account_domain_and_more"),
    ]

    operations = [
        migrations.RunPython(delete_null_user_or_account),
    ]
