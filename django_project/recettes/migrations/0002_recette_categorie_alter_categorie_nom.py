# Generated by Django 5.1.4 on 2024-12-13 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recettes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recette',
            name='categorie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recettes', to='recettes.categorie'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categorie',
            name='nom',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]