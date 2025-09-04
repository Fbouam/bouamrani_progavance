from django.urls import path
from . import views
urlpatterns = [
path("", views.home, name="home"),
path("contactus", views.contactUs, name="contactus"),
path("aboutus", views.aboutUs, name="aboutus")
]