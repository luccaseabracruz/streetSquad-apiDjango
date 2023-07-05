from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator, EmailValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'contact',
            'full_name',
            'is_seller',
            'is_superuser',
            'created_at',
            'updated_at'
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
            'is_superuser',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'validators': [
                    RegexValidator(
                        regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]+$',
                        message='The password must contain at least one uppercase letter, one lowercase letter, one number and one special character.'
                    )
                ]
            },
            'email': {
                'validators': [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with this email address has already been created."
                    ),
                    EmailValidator(
                        message='The email must be valid.'
                    )
                ]
            },
            'username': {
                'validators': [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with this username address has already been created."
                    )
                ]
            },
            'is_seller': {'required': False},
        }

    def create(self, validated_data: dict):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == 'password':
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()
        return instance


class ResponseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'contact',
            'email',
            'full_name',
        ]
