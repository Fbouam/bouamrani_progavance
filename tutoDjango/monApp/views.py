from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Produit, Categorie, Statut
from . import models as models_module

def home(request):
    if request.GET and request.GET.get("test"):
        raise Http404
    return HttpResponse("Bonjour Monde")

def contactus(request):
    return render(request, 'monApp/contact.html')

def aboutus(request):
    return render(request, 'monApp/about.html')

def ListProduits(request):
    prdts = Produit.objects.all()
    return render(request, 'monApp/list_produits.html',{'prdts': prdts})

def ListCategories(request):
    cats = Categorie.objects.all()
    return render(request, 'monApp/list_categories.html', {'cats': cats})

def ListStatuts(request):
    stats = Statut.objects.all()
    return render(request, 'monApp/list_statuts.html', {'stats': stats})

def ListRayons(request):
    Rayon = getattr(models_module, 'Rayon', None)
    if Rayon is None:
        rayons = []
    else:
        rayons = Rayon.objects.all()
    return render(request, 'monApp/list_rayons.html', {'rayons': rayons})