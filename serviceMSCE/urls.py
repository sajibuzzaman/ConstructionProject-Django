from django.urls import path
from . import views

urlpatterns = [
    path('', views.ServicesView, name="services"),
    path('team/', views.MSCETeamView, name="team")
]