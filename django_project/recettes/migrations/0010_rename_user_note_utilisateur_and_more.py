# Generated by Django 5.1.4 on 2025-01-03 17:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recettes', '0009_recette_note_moyenne'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='user',
            new_name='utilisateur',
        ),
        migrations.AlterUniqueTogether(
            name='note',
            unique_together={('utilisateur', 'recette')},
        ),
        migrations.AlterField(
            model_name='note',
            name='valeur',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
