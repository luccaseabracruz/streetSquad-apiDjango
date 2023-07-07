from rest_framework import serializers
from .models import Cart, CartProducts
from users.serializers import ResponseUserSerializer
from products.serializers import ProductSerializer
from products.models import Product


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
        extra_kwargs = {'quantity': {'required': True}}

    def get_total(self, obj):
        return obj.quantity * obj.product.price

    def check_stock_quantity(self, stock_quantity: int, request_quantity: int, cart_quantity=None):
        if request_quantity > stock_quantity:
            raise serializers.ValidationError({'detail': 'A quantidade solicitada não está disponível em estoque'})
        if cart_quantity:
            if cart_quantity + request_quantity > stock_quantity:
                raise serializers.ValidationError({'detail': 'A quantidade solicitada somada à quantidade em seu carrinho não está disponível em estoque'})

    def create(self, validated_data):
        Cart.objects.get_or_create(user=self.context["request"].user)
        cart = Cart.objects.get(user=self.context["request"].user)
        product = Product.objects.get(id=self.context.get('view').kwargs.get('pk'))
        quantity = validated_data.get('quantity')
        seller = product.user.id
        try:
            cart_product = CartProducts.objects.get(cart=cart, product=product)
            self.check_stock_quantity(product.stock_quantity, quantity, cart_product.quantity)
            cart_product.quantity += quantity
            cart_product.save()
        except CartProducts.DoesNotExist:
            cart_product = CartProducts.objects.create(
                cart=cart, product=product, quantity=quantity, seller=seller
            )
        # serializer = self.__class__(instance=cart_product)
        return cart_product

    def update(self, instance, validated_data):
        cart_product = CartProducts.objects.get(id=self.context.get("view").kwargs.get("pk"))
        quantity = validated_data.get("quantity")
        product = Product.objects.get(id=cart_product.product.id)
        self.check_stock_quantity(product.stock_quantity, quantity)
        return super().update(instance, validated_data)
