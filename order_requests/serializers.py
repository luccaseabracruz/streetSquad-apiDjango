from rest_framework import serializers
from carts.models import Cart, CartProducts
from products.serializers import ProductSerializer
from users.models import User
from .models import Request, RequestProducts
from django.core.mail import send_mail
from django.conf import settings


class RequestProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

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

        seller_orders = {}

        for item in carts_products:
            seller_id = item.seller
            if seller_id in seller_orders:
                seller_orders[seller_id].append(item)
            else:
                seller_orders[seller_id] = [item]

        for seller_id, products in seller_orders.items():
            request = Request.objects.create(**validated_data, seller=seller_id)

            for product in products:
                RequestProducts.objects.create(
                    request=request,
                    quantity=product.quantity,
                    product=product.product,
                    seller=product.seller,
                )
        return request

    def update(self, instance, validated_data):
        request_id = self.context.get("view").kwargs.get("pk")
        items = Request.objects.filter(buyer_id=request_id)
        for item in items:
            item.status = "concluido"
            item.save()
            send_mail(
                subject="Atualização do pedido",
                message=f"Olá, {instance.buyer.full_name}! Seu pedido foi concluído com sucesso.",
                recipient_list=[instance.buyer.email],
                from_email=settings.EMAIL_HOST_USER,
                fail_silently=False
            )
        return super().update(instance, validated_data)
