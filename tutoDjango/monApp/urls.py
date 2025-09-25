
from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.HomeView.as_view()),
    #path('', views.home, name='home'),
    #path('home/', views.home, name='home'),
    #path('home/<param>', views.home, name='home'),
    path("contactus/", views.ContactView.as_view()),
    #path('contactus', views.contactus, name='contactus'),
    path('aboutus/', views.AboutView.as_view()),
    #path('aboutus', views.aboutus, name='aboutus'),
    path('produits/', views.ListProduits, name='list_produits'),
    path('categories/', views.ListCategories, name='list_categories'),
    path('statut/', views.ListStatuts, name='list_statut'),
    
]