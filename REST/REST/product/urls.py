from django.urls import path
from .views import (
    ProductListCreateView,
    ProductRetrieveUpdateDestroy,
)

urlpatterns = [
    path('products', ProductListCreateView.as_view(), name='product_list_create'),
    path('products/<int:pk>', ProductRetrieveUpdateDestroy.as_view(), name='product_detail'),
]
