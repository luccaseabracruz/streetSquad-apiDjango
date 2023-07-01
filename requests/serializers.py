from rest_framework import serializers
from .models import Request


class RequestSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Request
        fields = [
            "id",
            "status",
            "product_quantily",
            "created_at",
            "updated_at",
        ]
