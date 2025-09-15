from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import Produit, Categorie, Statut

def home(request, param='Django'):
    if request.GET and request.GET["test"]:
        raise Http404
    return HttpResponse("Bonjour Monde")

def contactus(request):
    return HttpResponse('<h1>Contact Us!</h1>')

def aboutus(request):
    return HttpResponse('<h1>About Us!</h1>')

def ListProduits(request):
    prdts = Produit.objects.all()
    return render(request, 'monApp/list_produits.html',{'prdts': prdts})

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