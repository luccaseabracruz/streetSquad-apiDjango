from rest_framework import serializers
from .models import Address
from users.serializers import UserSerializer
from .exceptions import VerifyAddress


class AddressSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Address
        fields = [
            'id',
            'zip_code',
            'street',
            'number',
            'city',
            'state',
            'country',
            'user'
        ]
        read_only_fields = [
            'id',
            'user',
        ]

    # def create(self, validated_data):
    #     user = validated_data["user"]
    #     if hasattr(user, "address"):
    #         import ipdb; ipdb.set_trace()
    #         raise VerifyAddress()

    #     return Address.objects.create(**validated_data)

    def create(self, validated_data):
        user = validated_data["user"]
        if hasattr(user, "address"):
            raise VerifyAddress()
        
        return super().create(validated_data)
