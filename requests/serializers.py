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
        read_only_fields = ["created_at", "updated_at"]

    def create(self, validated_data):
        stock_quantity = validated_data["product"].stock_quantity
        product_quantily = validated_data["product_quantily"]

        validated_data["product"].stock_quantity = stock_quantity - product_quantily
        validated_data["product"].save()
        
        return Request.objects.create(**validated_data)
