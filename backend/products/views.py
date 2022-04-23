from django.shortcuts import render

# Create your views here.


# Generic view ------>>>


from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

"""Detail API View"""
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_view = ProductDetailAPIView.as_view()



"""Create API View"""

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)


product_create_view = ProductCreateAPIView.as_view()