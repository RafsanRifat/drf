from rest_framework import serializers
from .models import Product


def validate_title(value):
    qs = Product.objects.filter(title__exact=value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already a peoduct name")
    return value
