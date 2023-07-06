from rest_framework import serializers
from .models import Request


class ResponseOrderDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = [
            "status",
            "product_quantity",
            "created_at",
            "updated_at",
            "product",
        ]
        read_only_fields = ["created_at", "updated_at", "status"]


class RequestSerializer(serializers.ModelSerializer):
    order_data = ResponseOrderDataSerializer(read_only=True, many=True)

    class Meta:
        model = Request
        fields = [
            "id",
            "status",
            "product_quantily",
            "created_at",
            "updated_at",
            "product",
            "order_data",
        ]

        read_only_fields = ["id", "created_at", "updated_at", "order_data"]

        write_only_fields = ["product_quantily", "product"]

