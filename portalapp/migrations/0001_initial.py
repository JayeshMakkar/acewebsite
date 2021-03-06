# Generated by Django 2.1 on 2018-08-08 18:58

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
                ('course', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('email_id', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10)),
                ('is_member', models.BooleanField(default=False)),
                ('is_core', models.BooleanField(default=False)),
                ('task_submitted', models.BooleanField(default=False)),
                ('submission_url', models.TextField(blank=True)),
                ('section', models.CharField(blank=True, max_length=3, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('behance', models.URLField(blank=True, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now=True)),
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
                ('did_by', models.ManyToManyField(blank=True, null=True, to='portalapp.ACEUserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='aceuserprofile',
            name='task_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portalapp.Tasks'),
        ),
        migrations.AlterUniqueTogether(
            name='aceuserprofile',
            unique_together={('name', 'enroll_number', 'email_id', 'task_id')},
        ),
    ]
