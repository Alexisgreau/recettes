# Generated by Django 5.1.4 on 2024-12-17 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recettes', '0006_recette_ingredients_recette_temps_cuisson'),
    ]

    operations = [
        migrations.AddField(
            model_name='recette',
            name='etapes',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]