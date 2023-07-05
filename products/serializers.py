from rest_framework import serializers
from .models import Product
from users.serializers import ResponseUserSerializer


class ProductSerializer(serializers.ModelSerializer):
    seller = ResponseUserSerializer(read_only=True, source="user")

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "stock_quantity",
            "created_at",
            "updated_at",
            "category",
            "image_url",
            "seller"
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "seller",
        ]

        write_only_fields = [
            "user"
        ]

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
