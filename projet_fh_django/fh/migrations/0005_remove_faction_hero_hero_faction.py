# Generated by Django 4.0.4 on 2022-05-17 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fh', '0004_faction_hero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faction',
            name='hero',
        ),
        migrations.AddField(
            model_name='hero',
            name='faction',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='fh.faction'),
        ),
    ]
