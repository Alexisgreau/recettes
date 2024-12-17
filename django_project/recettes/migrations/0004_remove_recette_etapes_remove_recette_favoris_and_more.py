# Generated by Django 5.1.4 on 2024-12-17 09:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recettes', '0003_recette_favoris'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recette',
            name='etapes',
        ),
        migrations.RemoveField(
            model_name='recette',
            name='favoris',
        ),
        migrations.RemoveField(
            model_name='recette',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='recette',
            name='temps_cuisson',
        ),
        migrations.AlterField(
            model_name='recette',
            name='categorie',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='recette',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='recette',
            name='titre',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Favori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('recette', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoris', to='recettes.recette')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoris', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'recette')},
            },
        ),
    ]
