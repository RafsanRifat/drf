from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'pk',
            'url',
            'title',
            'price',
            'content',
            'sale_price',
            'my_discount',
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-detail', kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        # print(obj.id)
        # try:
        #     return obj.get_discount()
        # except:
        #     return None
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
