# Generated by Django 3.2.6 on 2021-09-16 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rater', '0002_alter_uploadanswer_examinfos'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadanswer',
            name='testrealname',
            field=models.CharField(default='', max_length=30),
        ),
    ]