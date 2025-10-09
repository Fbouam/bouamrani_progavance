from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('home/', views.HomeView.as_view(), name='home'),

    # Produits
    path('produits/', views.ProduitListView.as_view(), name='lst_prdts'),
    path('produit/<int:pk>/', views.ProduitDetailView.as_view(), name='dtl_prdt'),
    path('produits/creer/', views.ProduitCreateView.as_view(), name='crt-prdt'),
    path('produit/<int:pk>/modifier/', views.ProduitUpdateView.as_view(), name='prdt-chng'),
    path('produit/<int:pk>/delete/', views.ProduitDeleteView.as_view(), name='dlt-prdt'),

    # Catégories
    path('categories/', views.CategorieListView.as_view(), name='lst_cats'),
    path('categorie/creer/', views.CategorieCreateView.as_view(), name='crt_cat'),
    path('categorie/<int:pk>/', views.CategorieDetailView.as_view(), name='dtl-cat'),
    path('categorie/<int:pk>/modifier/', views.CategorieUpdateView.as_view(), name='upd-cat'),
    path('categorie/<int:pk>/delete/', views.CategorieDeleteView.as_view(), name='dlt-cat'),

    # Statuts
    path('statuts/', views.StatutListView.as_view(), name='lst_stats'),
    path('statut/creer/', views.StatutCreateView.as_view(), name='crt_stat'),
    path('statut/<int:pk>/', views.StatutDetailView.as_view(), name='dtl_stat'),
    path('statut/<int:pk>/modifier/', views.StatutUpdateView.as_view(), name='upd_stat'),
    path('statut/<int:pk>/delete/', views.StatutDeleteView.as_view(), name='dlt_stat'),

    # Rayons
    path('rayons/', views.RayonListView.as_view(), name='lst_rayons'),
    path('rayon/creer/', views.RayonCreateView.as_view(), name='crt_rayon'),
    path('rayon/<int:pk>/', views.RayonDetailView.as_view(), name='dtl-rayon'),
    path('rayon/<int:pk>/modifier/', views.RayonUpdateView.as_view(), name='upd-rayon'),
    path('rayon/<int:pk>/delete/', views.RayonDeleteView.as_view(), name='dlt-rayon'),
]