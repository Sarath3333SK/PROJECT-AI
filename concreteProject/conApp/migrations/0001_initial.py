# Generated by Django 3.0.2 on 2020-09-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='conModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cement', models.FloatField()),
                ('slag', models.FloatField()),
                ('flyash', models.FloatField()),
                ('water', models.FloatField()),
                ('superplasticizer', models.FloatField()),
                ('coarseaggreate', models.FloatField()),
                ('fineaggregate', models.FloatField()),
                ('age', models.FloatField()),
            ],
        ),
    ]
