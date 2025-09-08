from django.db import models
from datetime import date

class Categorie(models.Model):
    idCat = models.AutoField(primary_key=True)
    nomCat = models.CharField(max_length=100)

    def __str__(self):
        return self.nomCat

class Statut(models.Model):
    idStatut = models.AutoField(primary_key=True)
    libelleStatut = models.CharField(max_length=100)
          
    def __str__(self):
        return self.libelleStatus

class Produit(models.Model):
    refProd = models.AutoField(primary_key=True)
    intituleProd = models.CharField(max_length=200)
    prixUnitaireProd = models.DecimalField(max_digits=10, decimal_places=2)
    date_fabr = models.DateTimeField(default= date.today)
    # Relation CIF : chaque produit appartient à 1 catégorie(0,N côté catégorie -> 1, 1 côté produit)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="produits", null=True, blank=True)
    status = models.ForeignKey(Statut, on_delete=models.CASCADE, related_name="produits_status",null=True, blank=True)


    def __str__(self):
        return self.intituleProd
    
class Rayon(models.Model):
    refRay = models.AutoField(primary_key=True)
    nomRay = models.CharField(max_length=100)
    def __str__(self):
        return self.nomRay
    
class Contenir(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name="contenir_produit")
    rayon = models.ForeignKey(Rayon, on_delete=models.CASCADE, related_name="contenir_rayon")
    Qte = models.PositiveIntegerField()

    class Meta:
        unique_together = ('produit', 'rayon')

    def __str__(self):
        return f"{self.produit} dans {self.rayon} (Qte: {self.Qte})"
    
