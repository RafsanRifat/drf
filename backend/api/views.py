"""
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer


# Create your views here.

# def api_home(request, *args, **kwargs):
#     body = request.body  # Eikhane body variable a data string Json format a ache orthat '{"key":"value"}' amon quotation er moddhe ache
#     data = {}  # empty python dictionary declare kora holo
#     try:
#         data = json.loads(body)  # string og json data ----> python Dictionary
#     except:
#         pass
#     print(data.keys())
#     print(request.headers)
#     print(request.GET)      # params er value gulo pawa jabe
#     print(request.POST)        # params er value gulo pawa jabe
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    # instance = Product.objects.all().order_by("?").first()  # this will select all objects randomly one by one
    # # data = {}
    # if instance:
    #     # data['id'] = instance.id
    #     # data['title'] = instance.title
    #     # data['price'] = instance.price
    #     # data['content'] = instance.content
    #
    #     data = ProductSerializer(instance).data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()  # ei instance ta r serialized nai. eta database a save howa object
        # print(instance)
        # data = serializer.data
        return Response(serializer.data)



    #Goal is to take django model instance >>> turn indo python Dictionary >>> return Json to client


"""
# Generic view ------>>>


from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
product_detail_view = ProductDetailAPIView.as_view()
