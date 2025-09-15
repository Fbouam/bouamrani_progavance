from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contactus, name='contact'),
    path('about/', views.aboutus, name='about'),
    path('produits/', views.ListProduits, name='produits'),
    path('categories/', views.ListCategories, name='categories'),
    path('statuts/', views.ListStatuts, name='statuts'),
    path('rayons/', views.ListRayons, name='rayons'),
]