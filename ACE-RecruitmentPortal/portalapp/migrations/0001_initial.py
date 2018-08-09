# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-06 04:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ACEUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enroll_number', models.CharField(max_length=11)),
                ('course', models.CharField(choices=[('a', 'BCA'), ('b', 'MCA')], max_length=1)),
                ('email_id', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10)),
                ('is_member', models.BooleanField(default=False)),
                ('is_core', models.BooleanField(default=False)),
                ('task_submitted', models.BooleanField(default=False)),
                ('submission_url', models.TextField(blank=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('task_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=30)),
                ('submission_deadline', models.CharField(max_length=10)),
                ('difficulty_level', models.CharField(max_length=50)),
                ('difficulty_value', models.CharField(default='Easy', max_length=30)),
                ('task_description', models.TextField()),
                ('total_submissions', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='aceuserprofile',
            unique_together=set([('name', 'enroll_number', 'email_id')]),
        ),
    ]