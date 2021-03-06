# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-22 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jtitle', models.CharField(max_length=255)),
                ('jcompany', models.CharField(max_length=255)),
                ('jtype', models.CharField(max_length=255)),
                ('jpost_url', models.CharField(max_length=255)),
                ('jcompany_url', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=255)),
                ('clong', models.DecimalField(decimal_places=2, max_digits=4)),
                ('clatt', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='jobs_app.Location'),
        ),
    ]
