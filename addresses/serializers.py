from rest_framework import serializers
from .models import Address
from users.serializers import UserSerializer

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
