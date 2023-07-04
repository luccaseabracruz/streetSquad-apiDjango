from rest_framework import serializers
from .models import Product
from users.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

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
            "user"
        ]
        read_only_fields = ["id",  "created_at", "updated_at"]

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
