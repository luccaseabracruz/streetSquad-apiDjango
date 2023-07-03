from rest_framework import serializers
from .models import Request
from products.serializers import ProductSerializer


class RequestSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True)

    class Meta:
        model = Request
        fields = [
            "id",
            "status",
            "product_quantily",
            "created_at",
            "updated_at",
            "products",
        ]
        read_only_fields = ["id", "status", "created_at", "updated_at"]
