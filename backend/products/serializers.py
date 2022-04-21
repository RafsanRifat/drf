from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'price',
            'content',
            'sale_price',
            'my_discount',
        ]

    def get_my_discount(self, obj):
        # print(obj.id)
        try:
            return obj.get_discount()
        except:
            return None
