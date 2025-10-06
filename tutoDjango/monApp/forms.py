from django import forms
from django.shortcuts import render
from .models import Produit, Categorie, Statut, Rayon

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        # fields = '__all__'
        exclude = ('categorie', 'status')

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nomCat']  # retirer 'description' qui n'existe pas dans le modèle
        widgets = {
            'nomCat': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }

class StatutForm(forms.ModelForm):
    class Meta:
        model = Statut
        fields = ['libelleStatut']
        widgets = {
            'libelleStatut': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }

class RayonForm(forms.ModelForm):
    class Meta:
        model = Rayon
        fields = ['nomRay']
        widgets = {
            'nomRay': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }