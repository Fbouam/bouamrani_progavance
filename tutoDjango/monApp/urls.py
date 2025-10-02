from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.HomeView.as_view(), name='home'),
    #path('', views.home, name='home'),
    #path('home/', views.home, name='home'),
    path('home/<param>/', views.HomeParamView.as_view()),
    path("contactus/", views.ContactView),
    #path('contactus', views.contactus, name='contactus'),
    path('aboutus/', views.AboutView.as_view()),
    #path('aboutus', views.aboutus, name='aboutus'),
    #path('produits/', views.ListProduits, name='list_produits'),
    path("produits/",views.ProduitListView.as_view(),name="lst_prdts"),
    path("produit/<pk>/" ,views.ProduitDetailView.as_view(), name="dtl_prdt"),
    path("categories/", views.CategorieListView.as_view(), name="lst_cats"),
    path('categorie/<int:pk>/', views.CategorieDetailView.as_view(), name='dtl_cat'),
    path("statuts/", views.StatutListView.as_view(), name="lst_stats"),
    path("statut/<pk>/", views.StatutDetailView.as_view(), name="dtl_stat"),
    path("rayons/", views.RayonListView.as_view(), name="lst_rayons"),
    path("rayon/<pk>/", views.RayonDetailView.as_view(), name="dtl_rayon"),
    path('categories/', views.ListCategories, name='list_categories'),
    path('statut/', views.ListStatuts, name='list_statut'),
    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),
    path('email-sent/', views.EmailSentView.as_view(), name='email-sent'),
]