from django.urls import path
from . import views

urlpatterns = [
    path('visits/', views.visit_count_view, name='visit_count'),
]
