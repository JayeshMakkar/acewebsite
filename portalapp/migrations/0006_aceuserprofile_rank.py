# Generated by Django 2.1.1 on 2018-12-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0005_auto_20180910_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='aceuserprofile',
            name='rank',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]