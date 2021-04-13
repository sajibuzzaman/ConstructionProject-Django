from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.Contact, name='Contact'),
    path('projects/', views.Allprojects, name='projects'),
    path('project/<slug:slug>/', views.project_single, name='project_single'),
    path('about/', views.AboutUs, name='about'),
]