from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from .validators import validate_title


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField()
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
    )
    title = serializers.CharField(validators=[validate_title])

    class Meta:
        model = Product
        fields = [
            'id',
            'pk',
            'url',
            'edit_url',
            'title',
            'price',
            'content',
            'sale_price',
            'my_discount',
        ]

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-update', kwargs={"pk": obj.pk}, request=request)

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
