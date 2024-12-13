from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)  # Le nom de la catégorie doit être unique

    def __str__(self):
        return self.nom


class Recette(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()  # Liste des ingrédients
    etapes = models.TextField()  # Étapes de préparation
    image = models.ImageField(upload_to='recettes/', null=True, blank=True)
    temps_preparation = models.IntegerField()  # Temps en minutes
    temps_cuisson = models.IntegerField()  # Temps en minutes
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="recettes")  # Lien vers une catégorie

    def __str__(self):
        return self.titre
