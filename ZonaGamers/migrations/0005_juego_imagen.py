# Generated by Django 5.0.6 on 2024-07-04 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZonaGamers', '0004_alter_juego_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='juegos/'),
        ),
    ]
