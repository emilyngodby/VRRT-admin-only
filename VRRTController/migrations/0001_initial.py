# Generated by Django 3.1.3 on 2020-11-30 01:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SurveyName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular survey', primary_key=True, serialize=False)),
                ('PainScoreStart', models.IntegerField(max_length=2)),
                ('PainScoreEnd', models.IntegerField(max_length=2)),
                ('survey', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='VRRTController.survey')),
            ],
        ),
    ]