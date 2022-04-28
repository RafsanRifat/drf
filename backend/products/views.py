from django.http import Http404
from django.shortcuts import render

# Create your views here.


# Generic view ------>>>


from rest_framework import generics, permissions, authentication
from .models import Product
from .serializers import ProductSerializer
from api.permissions import IsStaffEditorPermission
from rest_framework import decorators
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

"""Detail API View"""


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_view = ProductDetailAPIView.as_view()

"""Delete API View"""


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'


product_delete_view = ProductDeleteAPIView.as_view()

"""Update API View"""


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    def perform_update(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)


product_update_view = ProductUpdateAPIView.as_view()

"""Create API View"""


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.TokenAuthentication
                              ]
    permission_classes = [permissions.IsAdminUser,
                          IsStaffEditorPermission,
                          ]

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)


product_create_view = ProductListCreateAPIView.as_view()

"""     custom view    """

# @api_view(['GET', 'POST'])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method
#
#     if method == "GET":
#         # url_args
#
#         #  detail view
#         if pk is not None:
#             try:
#                 # obj = Product.objects.get(pk=pk)
#                 obj = get_object_or_404(Product, pk=pk)
#                 data = ProductSerializer(obj)
#                 return Response(data.data)
#             except:
#                 return Response({"Error": "This item doesn't exist"})
#
#         # list view
#         queryset = Product.objects.all()
#         data = ProductSerializer(queryset, many=True).data
#         return Response(data)
#         pass
#
#     # create view
#     if method == "POST":
#         # create an item
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content')
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#         # return Response({"invalid": "Not good data"}, status=400)
