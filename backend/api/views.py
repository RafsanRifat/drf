from django.http import JsonResponse
import json


# Create your views here.

def api_home(request, *args, **kwargs):
    body = request.body  # Eikhane body variable a data string Json format a ache orthat '{"key":"value"}' amon quotation er moddhe ache
    data = {}  # empty python dictionary declare kora holo
    try:
        data = json.loads(body)  # string og json data ----> python Dictionary
    except:
        pass
    print(data.keys())
    print(request.headers)
    print(request.GET)      # params er value gulo pawa jabe
    print(request.POST)        # params er value gulo pawa jabe
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
