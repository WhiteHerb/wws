# Generated by Django 3.2.6 on 2021-09-16 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rater', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadanswer',
            name='examinfos',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
