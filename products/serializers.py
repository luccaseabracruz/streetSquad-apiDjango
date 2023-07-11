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
        self.verify_stock(validated_data['stock_quantity'])
        return Product.objects.create(**validated_data)

    def verify_stock(self, stock_quantity):
        if stock_quantity <= 0 or stock_quantity >= 10000:
            raise serializers.ValidationError(
                {"detail": "It is not possible to register this quantity"}
            )
