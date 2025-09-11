from django.shortcuts import render
from django.http import HttpResponse
from .models import Produit, Categorie, Statut
def home(request, param='Django'):
    return HttpResponse(f"<h1>Bonjour {param} !</h1>")

def contactus(request):
    return HttpResponse('<h1>Contact Us!</h1>')

def aboutus(request):
    return HttpResponse('<h1>About Us!</h1>')

def ListProduits(request):
    prdts = Produit.objects.all()
    if not prdts:
        html = "<h1>Liste des produits</h1><p>Aucun produit trouvé.</p>"
    else:
        li_items = "".join([f"<li>{p.intituleProd}</li>" for p in prdts])
        html = f"""
        <h1>Liste des produits</h1>
        <ul>
            {li_items}
        </ul>
        """
    return HttpResponse(html)

def ListCategories(request):
    cats = Categorie.objects.all()
    if not cats:
        html = "<h1>Liste des catégories</h1><p>Aucune catégorie trouvée.</p>"
    else:
        li_items = "".join([f"<li>{c.nomCat}</li>" for c in cats])
        html = f"""
        <h1>Liste des catégories</h1>
        <ul>
            {li_items}
        </ul>
        """
    return HttpResponse(html)

def ListStatuts(request):
    stats = Statut.objects.all()
    if not stats:
        html = "<h1>Liste des statuts</h1><p>Aucun statut trouvé.</p>"
    else:
        li_items = "".join([f"<li>{s.libelleStatut}</li>" for s in stats])
        html = f"""
        <h1>Liste des statuts</h1>
        <ul>
            {li_items}
        </ul>
        """
    return HttpResponse(html)