# Generated by Django 4.0.4 on 2022-05-13 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fh', '0002_faction_faction_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Nom', models.CharField(max_length=100)),
                ('Type', models.CharField(choices=[('gardien', 'Gardien'), ('tank', 'Tank'), ('assassin', 'Assassin'), ('hybride', 'Hybride')], default='facile', max_length=10)),
                ('Difficulte', models.CharField(choices=[('facile', 'Facile'), ('intermédiaire', 'Intermédiare'), ('difficile', 'Difficile')], default='gardien', max_length=15)),
            ],
        ),
    ]
