from django.urls import path
from . import views, forms

urlpatterns = [
    path("home/", views.HomeView.as_view(), name='home'),
    #path('', views.home, name='home'),
    #path('home/', views.home, name='home'),
    path('home/<param>/', views.HomeParamView.as_view()),

    path("contactus/", views.ContactView),
    #path('contactus', views.contactus, name='contactus'),

    path('aboutus/', views.AboutView.as_view()),
    #path('aboutus', views.aboutus, name='aboutus'),

    path('produits/', views.ListProduits, name='lst_prdts'),
    path("produit/",views.ProduitCreate , name="crt-prdt"),
    path("produit/<pk>/update/",views.ProduitUpdateView.as_view(), name="prdt-chng"),
    path("produit/<pk>/" ,views.ProduitDetailView.as_view(), name="dtl_prdt"),
    path("produit/<pk>/delete/",views.ProduitDeleteView.as_view(), name="dlt-prdt"),

    path("categories/", views.CategorieListView.as_view(), name="lst_cats"),
    path('categorie/<int:pk>/', views.CategorieDetailView.as_view(), name='dtl_cat'),
    path('categorie/creer/', views.CategorieCreateView.as_view(), name='crt_cat'),
    path('categorie/<int:pk>/', views.CategorieDetailView.as_view(), name='dtl_cat'),
    path('categorie/<int:pk>/modifier/', views.CategorieUpdateView.as_view(), name='upd_cat'),
    path('categorie/<int:pk>/delete/', views.CategorieDeleteView.as_view(), name='dlt_cat'),
    # path('categories/', views.ListCategories, name='list_categories'),


    path("statut/<pk>/", views.StatutDetailView.as_view(), name="dtl_stat"),
    path("statuts/", views.StatutListView.as_view(), name="lst_stats"),
    path('statut/creer/', views.StatutCreateView.as_view(), name='crt_stat'),
    path("statut/<int:pk>/", views.StatutDetailView.as_view(), name="dtl_stat"),
    path("statut/<int:pk>/modifier/", views.StatutUpdateView.as_view(), name="upd_stat"),
    path("statut/<int:pk>/delete/", views.StatutDeleteView.as_view(), name="dlt_stat"),

    path("rayons/", views.RayonListView.as_view(), name="lst_rayons"),
    path('rayon/creer/', views.RayonCreateView.as_view(), name='crt_rayon'),
    path("rayon/<int:pk>/", views.RayonDetailView.as_view(), name="dtl_rayon"),
    path("rayon/<int:pk>/modifier/", views.RayonUpdateView.as_view(), name="upd_rayon"),
    path("rayon/<int:pk>/delete/", views.RayonDeleteView.as_view(), name="dlt_rayon"),

    path('statut/', views.ListStatuts, name='list_statut'),

    path('login/', views.ConnectView.as_view(), name='login'),

    path('register/', views.RegisterView.as_view(), name='register'),

    path('logout/', views.DisconnectView.as_view(), name='logout'),

    path('email-sent/', views.EmailSentView.as_view(), name='email-sent'),
    
]