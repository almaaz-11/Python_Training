from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# /api/products/ (list and create)
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        print("User: ", request.user, "Auth: ", request.auth)
        return super().list(request, args, **kwargs)

# /api/products/<id>/ (retrieve, update, delete)
class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer