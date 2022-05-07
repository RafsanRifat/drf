from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


class ProductViewsSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
