from rest_framework import serializers
from .models import Request
from products.serializers import ProductSerializer


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = [
            "id",
            "status",
            "product_quantily",
            "created_at",
            "updated_at",
            "product",
        ]
        read_only_fields = ["id", "status", "created_at", "updated_at"]
