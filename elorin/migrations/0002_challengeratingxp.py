# Generated by Django 2.2.9 on 2020-02-19 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elorin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeRatingXP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge', models.CharField(max_length=3)),
                ('xp', models.IntegerField()),
            ],
        ),
    ]
