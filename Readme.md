# Recettes Django

Une application web de gestion de recettes développée en **Python** avec le framework **Django**. Cette application permet aux utilisateurs de gérer des recettes et leurs catégories. Elle inclut des fonctionnalités comme l'ajout, la modification et l'affichage des recettes, ainsi qu'une barre de recherche pour retrouver facilement les recettes.

---

## Fonctionnalités

- **Ajout de Recettes** : Ajouter des recettes avec titre, description, ingrédients, étapes, temps de préparation et de cuisson, et une image.
- **Gestion des Catégories** : Associer chaque recette à une catégorie.
- **Affichage des Recettes** : Voir les recettes avec leur catégorie, description, temps et image.
- **Barre de Recherche** : Rechercher les recettes par titre.
- **Interface Moderne** : Utilisation de TailwindCSS pour une interface utilisateur simple et esthétique.

---

## Prérequis

Avant de démarrer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- **Python 3.8+**
- **pip** (gestionnaire de paquets Python)
- **Git**
- **Un serveur SQLite ou tout autre base de données compatible Django**
- **Un environnement virtuel (optionnel mais recommandé)**

---

## Installation

1. **Clonez le projet** :

   ```bash
   git clone https://github.com/votre-utilisateur/recettes-django.git
   cd recettes-django
   ```

2. **Créez un environnement virtuel** (optionnel mais recommandé) :

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Sur Linux/Mac
   venv\Scripts\activate      # Sur Windows
   ```

3. **Installez les dépendances** :

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurez l'application** :

   - Créez un fichier `.env` (ou utilisez les paramètres par défaut) pour définir vos variables d'environnement, comme la clé secrète ou les paramètres de base de données (si vous n'utilisez pas SQLite).

5. **Appliquez les migrations** pour configurer la base de données :

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Lancez le serveur de développement** :

   ```bash
   python manage.py runserver
   ```

7. **Accédez à l'application** dans votre navigateur à l'adresse suivante :

   ```
   http://127.0.0.1:8000/
   ```

---

## Fichiers Statique et Médias

- **Configuration pour les fichiers médias** : Assurez-vous que votre `settings.py` inclut :

  ```python
  MEDIA_URL = '/media/'
  MEDIA_ROOT = BASE_DIR / 'media'
  ```

- Pour servir les fichiers médias en local, ajoutez ceci dans `urls.py` :

  ```python
  from django.conf import settings
  from django.conf.urls.static import static

  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

---

## Dépendances Principales

- **Django** : Framework principal pour le développement.
- **TailwindCSS** : Utilisé pour styliser l'interface utilisateur.
- **Pillow** : Nécessaire pour la gestion des fichiers image.

La liste complète des dépendances est disponible dans le fichier `requirements.txt`.

---

## Fonctionnalités à Ajouter (Roadmap)

- Authentification des utilisateurs pour restreindre l'accès à certaines fonctionnalités.
- Ajout de fonctionnalités de commentaire sur les recettes.
- Recherche avancée par plusieurs champs.
- Gestion des favoris pour les recettes.

---

## Structure du Projet

- **models.py** : Définit les modèles pour les recettes et les catégories.
- **views.py** : Contient la logique pour gérer les pages et les requêtes.
- **templates/** : Dossiers contenant les fichiers HTML.
- **static/** : Fichiers CSS/JS et autres ressources statiques.

---

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez contribuer :

1. **Forkez** le projet.
2. Créez une **branche** pour vos modifications : `git checkout -b ma-branche`.
3. **Commitez** vos modifications : `git commit -m "Ajout d'une fonctionnalité"`.
4. **Poussez** vers votre dépôt forké : `git push origin ma-branche`.
5. Soumettez une **Pull Request**.

---

## Auteur

- **Nom** : Alexis GREAU

---