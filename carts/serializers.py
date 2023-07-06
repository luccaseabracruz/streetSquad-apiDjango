from rest_framework import serializers
from .models import Cart, CartProducts
from users.serializers import ResponseUserSerializer
from products.serializers import ProductSerializer
from products.models import Product
from users.models import User
import ipdb
from rest_framework.views import Response
from django.forms.models import model_to_dict


class CartSerializer(serializers.ModelSerializer):
    user = ResponseUserSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "user"]
        read_only_field = ["id"]


class CartProductsSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    cart = CartSerializer(read_only=True)

    class Meta:
        model = CartProducts
        fields = ["id", "cart", "quantity", "product"]
        extra_kwargs = {'quantity': {'required': True}} 

    def create(self, validated_data):
        cart = Cart.objects.get(user=self.context["request"].user)
        product = Product.objects.get(id=self.context.get('view').kwargs.get('pk'))
        quantity = validated_data.get('quantity')
        try:
            cart_product = CartProducts.objects.get(cart=cart, product=product)
            cart_product.quantity += quantity
            cart_product.save()
        except CartProducts.DoesNotExist:
            cart_product = CartProducts.objects.create(
                cart=cart, product=product, quantity=quantity
            )

        serializer = self.__class__(instance=cart_product)
        return serializer.data
