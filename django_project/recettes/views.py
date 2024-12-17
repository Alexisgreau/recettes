from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Categorie, Recette, Favori
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django import forms
from django.contrib.auth.models import User
from django.conf import settings
from .forms import RecetteForm

def home(request):
    rows = Recette.objects.all()

    # Vérifier si l'utilisateur est connecté pour récupérer ses favoris
    if request.user.is_authenticated:
        favoris_ids = Favori.objects.filter(user=request.user).values_list('recette_id', flat=True)
        favoris_ids = [int(f) for f in favoris_ids]  # Force les IDs à être des entiers
    else:
        favoris_ids = []  # Aucun favori pour un utilisateur non connecté

    # Renvoyer les données au template
    return render(request, 'recettes.html', {'rows': rows, 'favoris_ids': favoris_ids})


@login_required
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

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)

def profile(request):
    return render(request, 'profile.html')

@login_required
def toggle_favoris(request, pk):
    recette = get_object_or_404(Recette, pk=pk)
    favoris, created = Favori.objects.get_or_create(user=request.user, recette=recette)

    if not created:
        # Si le favori existe déjà, on le supprime (toggle)
        favoris.delete()
    return redirect('home')  # Redirige vers la vue principale

def fav_view(request):
    recettes = Recette.objects.filter(favoris__user=request.user)
    return render(request, 'favoris.html', {'rows': recettes})

def modifier_recette(request, pk):
    recette = get_object_or_404(Recette, pk=pk)
    if request.method == 'POST':
        form = RecetteForm(request.POST, request.FILES, instance=recette)
        if form.is_valid():
            form.save()
            return redirect('details', pk=recette.pk)  # Redirection vers la page de détails
    else:
        form = RecetteForm(instance=recette)
    return render(request, 'modifier_recette.html', {'form': form, 'recette': recette})