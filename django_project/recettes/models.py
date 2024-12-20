from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)  # Le nom de la catégorie doit être unique

    def __str__(self):
        return self.nom

# Modèle Recette existant
class Recette(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    categorie = models.ForeignKey(
        Categorie, on_delete=models.CASCADE, related_name='recettes'
    )  # Lien avec le modèle Categorie
    temps_preparation = models.IntegerField()
    temps_cuisson = models.IntegerField()
    ingredients = models.TextField()
    etapes = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    note_moyenne = models.FloatField(default=0.0)

    def __str__(self):
        return self.titre
    
    def update_note_moyenne(self):
        notes = self.notes.all()
        total_notes = notes.count()
        if total_notes > 0:
            moyenne = sum(note.valeur for note in notes) / total_notes
            self.note_moyenne = round(moyenne, 2)
        else:
            self.note_moyenne = 0.0  # Aucune note, la moyenne est 0
        self.save()  # Sauvegarde les changements




# Gestion des favoris
class Favori(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favoris'
    )  # L'utilisateur qui ajoute la recette aux favoris
    recette = models.ForeignKey(
        Recette, on_delete=models.CASCADE, related_name='favoris'
    )  # La recette ajoutée en favoris
    date_added = models.DateTimeField(auto_now_add=True)  # Date d'ajout aux favoris

    class Meta:
        unique_together = ('user', 'recette')  # Un utilisateur ne peut pas ajouter deux fois la même recette.

    def __str__(self):
        return f"{self.user.username} - {self.recette.titre}"
    
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE, related_name='notes')
    valeur = models.IntegerField(default=1)  # Valeur de la note (ex: 1 à 5)

    class Meta:
        unique_together = ('user', 'recette')  # Un utilisateur ne peut noter qu'une fois par recette

    def __str__(self):
        return f"{self.user.username} - {self.recette.titre} : {self.valeur}"