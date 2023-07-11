from rest_framework import serializers
from .models import Cart, CartProducts
from users.serializers import ResponseUserSerializer
from products.serializers import ProductSerializer
from products.models import Product
from django.shortcuts import get_object_or_404
from .exceptions import (
    VerifyOrderedQuantity,
    VerifyStockQuantity,
    VerifyStockQuantityAndOrderedQuantity,
)


class CartSerializer(serializers.ModelSerializer):
    user = ResponseUserSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "user"]
        read_only_field = ["id"]


class CartProductsSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    cart = CartSerializer(read_only=True)
    total = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CartProducts
        fields = ["id", "cart", "quantity", "product", "seller", "total"]
        extra_kwargs = {"quantity": {"required": True}}

    def get_total(self, obj):
        return obj.quantity * obj.product.price

    def create(self, validated_data):
        Cart.objects.get_or_create(user=self.context["request"].user)
        cart = Cart.objects.get(user=self.context["request"].user)
        product = get_object_or_404(
            Product, id=self.context.get("view").kwargs.get("pk")
        )
        quantity = validated_data.get("quantity")
        seller = product.user.id
        try:
            cart_product = CartProducts.objects.get(cart=cart, product=product)
            if quantity <= 0:
                raise VerifyOrderedQuantity()
            if quantity > product.stock_quantity:
                raise VerifyStockQuantity()
            if cart_product.quantity + quantity > product.stock_quantity:
                raise VerifyStockQuantityAndOrderedQuantity()
            cart_product.quantity += quantity
            cart_product.save()
        except CartProducts.DoesNotExist:
            cart_product = CartProducts.objects.create(
                cart=cart, product=product, quantity=quantity, seller=seller
            )
        return cart_product

    def update(self, instance, validated_data):
        cart_product = CartProducts.objects.get(
            id=self.context.get("view").kwargs.get("pk")
        )
        quantity = validated_data.get("quantity")
        product = Product.objects.get(id=cart_product.product.id)
        if quantity > product.stock_quantity:
            raise VerifyStockQuantity()
        # self.check_stock_quantity(product.stock_quantity, quantity)
        return super().update(instance, validated_data)
