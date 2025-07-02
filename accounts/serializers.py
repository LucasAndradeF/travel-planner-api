from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'date_joined']
        read_only_fields = ['id', 'date_joined']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[password_validation.validate_password])

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'date_joined']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']

        )

        return user
