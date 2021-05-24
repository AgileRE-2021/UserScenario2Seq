# Generated by Django 2.2.10 on 2021-05-24 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feature',
            fields=[
                ('id_feature', models.AutoField(primary_key=True, serialize=False)),
                ('feature_name', models.CharField(max_length=20)),
                ('user_story', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField()),
                ('last_updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id_project', models.AutoField(primary_key=True, serialize=False)),
                ('id_user', models.IntegerField(default=0)),
                ('project_name', models.CharField(max_length=20)),
                ('project_desc', models.TextField()),
                ('date_created', models.DateTimeField()),
                ('last_updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='scenario',
            fields=[
                ('id_scenario', models.AutoField(primary_key=True, serialize=False)),
                ('tipe', models.CharField(max_length=25)),
                ('content', models.CharField(max_length=75)),
                ('date_created', models.DateTimeField()),
                ('last_updated', models.DateTimeField()),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.feature')),
            ],
        ),
        migrations.AddField(
            model_name='feature',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project'),
        ),
    ]
