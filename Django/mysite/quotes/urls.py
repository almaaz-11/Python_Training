from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("passing_data/", views.passing_data, name="passing_data"),
]
