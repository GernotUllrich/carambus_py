# Generated by Django 4.2 on 2024-11-27 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carambus_py', '0006_alter_version_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('carambus_py.discipline',),
        ),
        migrations.AlterField(
            model_name='setting',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
