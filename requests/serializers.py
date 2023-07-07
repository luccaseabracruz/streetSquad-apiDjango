from rest_framework import serializers
from carts.models import Cart, CartProducts

from products.serializers import ProductSerializer
from users.models import User
from .models import Request, RequestProducts


class ResponseOrderDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = [
            "product_quantity",
            "created_at",
            "updated_at",
            "product",
        ]
        read_only_fields = ["created_at", "updated_at", "status"]


class RequestProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    """ request = RequestSerializer() """

    class Meta:
        model = RequestProducts
        fields = ["id", "quantity", "product", "request", "seller"]

        read_only_fields = ["id", "quantity", "product", "request"]


class RequestSerializer(serializers.ModelSerializer):
    product = RequestProductSerializer(
        read_only=True, many=True, source="requestproducts_set"
    )

    class Meta:
        model = Request
        fields = ["id", "status", "created_at", "updated_at", "product", "seller"]

        read_only_fields = ["id", "created_at", "updated_at", "order_data"]

    def create(self, validated_data):
        cart = Cart.objects.filter(user_id=validated_data["buyer"].id).first()
        carts_products = CartProducts.objects.filter(cart=cart)

        for product in carts_products:
            request = Request.objects.create(**validated_data, seller=product.seller)

            RequestProducts.objects.create(
                request=request,
                quantity=product.quantity,
                product=product.product,
                seller=product.seller,
            )
        return request