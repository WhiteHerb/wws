# Generated by Django 3.2.7 on 2021-09-07 04:32

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rater', '0002_auto_20210826_1154'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploaduseranswer',
            options={},
        ),
        migrations.RemoveField(
            model_name='uploadanswer',
            name='date_upload',
        ),
        migrations.RemoveField(
            model_name='uploadanswer',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='uploadanswer',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='uploaduseranswer',
            name='date_upload',
        ),
        migrations.AlterField(
            model_name='uploadanswer',
            name='examinfos',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None),
        ),
        migrations.AlterField(
            model_name='uploaduseranswer',
            name='wrong',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None),
        ),
    ]
