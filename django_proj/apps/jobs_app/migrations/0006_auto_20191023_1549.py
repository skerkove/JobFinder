# Generated by Django 2.1.5 on 2019-10-23 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_app', '0005_auto_20191023_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='jcompany_url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
