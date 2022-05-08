from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField()
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
    )

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

    def validate_title(self, value):
        qs = Product.objects.filter(title__exact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a peoduct name")
        return value

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
