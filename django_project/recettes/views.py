from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Categorie, Recette
from django.db.models import Q

def home(request):
    recettes = Recette.objects.all()  # Récupère toutes les recettes

    # Gestion de la recherche
    query = request.GET.get('search', '')
    if query:
        recettes = recettes.filter(
            Q(titre__icontains=query) |
            Q(description__icontains=query) |
            Q(ingredients__icontains=query) |
            Q(etapes__icontains=query) |
            Q(categorie__nom__icontains=query)
        )

    return render(request, 'recettes.html', {'rows': recettes})



def manage(request):
    if request.method == 'POST':
        # Récupère les données du formulaire
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        etapes = request.POST.get('etapes')
        temps_preparation = request.POST.get('temps_preparation')
        temps_cuisson = request.POST.get('temps_cuisson')
        categorie_id = request.POST.get('categorie')  # ID de la catégorie sélectionnée
        image = request.FILES.get('image')

        # Vérifie que tous les champs obligatoires sont renseignés
        if not titre or not description or not ingredients or not etapes or not temps_preparation or not categorie_id:
            messages.error(request, 'Tous les champs obligatoires doivent être remplis.')
            return redirect('manage')

        # Récupère l'objet catégorie
        try:
            categorie = Categorie.objects.get(id=categorie_id)
        except Categorie.DoesNotExist:
            messages.error(request, "La catégorie sélectionnée n'existe pas.")
            return redirect('manage')

        # Crée et sauvegarde la recette
        recette = Recette(
            titre=titre,
            description=description,
            ingredients=ingredients,
            etapes=etapes,
            temps_preparation=temps_preparation,
            temps_cuisson=temps_cuisson,
            categorie=categorie,
            image=image
        )
        recette.save()
        messages.success(request, 'Recette ajoutée avec succès !')
        return redirect('home')  # Redirige vers la page d'accueil après ajout

    # Si GET, affiche le formulaire
    categories = Categorie.objects.all()
    return render(request, 'manage.html', {'categories': categories}) 

def add_category(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')

        if nom:
            Categorie.objects.create(nom=nom)
            messages.success(request, 'Catégorie ajoutée avec succès !')
            return redirect('manage')
        else:
            messages.error(request, 'Le nom de la catégorie est obligatoire.')

    return render(request, 'manage_cat.html')

def details(request, pk):
    recette = Recette.objects.get(pk=pk)
    return render(request, 'details.html', {'recette': recette})