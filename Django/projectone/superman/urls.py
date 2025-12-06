from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.all_superhero, name='all_superhero'),
]