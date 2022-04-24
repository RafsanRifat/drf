from django.http import Http404
from django.shortcuts import render

# Create your views here.


# Generic view ------>>>


from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework import decorators
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

"""Detail API View"""


#
# class ProductDetailAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# product_detail_view = ProductDetailAPIView.as_view()
#
# """Create API View"""
#
#
# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def perform_create(self, serializer):
#         print(serializer.validated_data)
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content')
#         if content is None:
#             content = title
#         serializer.save(content=content)
#
#
# product_create_view = ProductListCreateAPIView.as_view()


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        # url_args

        #  detail view
        if pk is not None:
            try:
                obj = Product.objects.get(pk=pk)
                data = ProductSerializer(obj)
                return Response(data.data)
            except:
                return Response({"Error": "This item doesn't exist"})

        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
        pass

    # create view
    if method == "POST":
        # create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if content is None:
                content = title
            serializer.save(content=content)
        # return Response({"invalid": "Not good data"}, status=400)
