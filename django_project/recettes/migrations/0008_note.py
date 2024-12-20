# Generated by Django 5.1.4 on 2024-12-18 07:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recettes', '0007_recette_etapes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.IntegerField(default=1)),
                ('recette', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='recettes.recette')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'recette')},
            },
        ),
    ]
