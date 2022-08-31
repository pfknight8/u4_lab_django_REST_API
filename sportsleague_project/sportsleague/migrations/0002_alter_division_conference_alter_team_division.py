# Generated by Django 4.1 on 2022-08-31 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportsleague', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='division',
            name='conference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conferences', to='sportsleague.conference'),
        ),
        migrations.AlterField(
            model_name='team',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='divisions', to='sportsleague.division'),
        ),
    ]
