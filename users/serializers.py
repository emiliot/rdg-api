from rest_framework import serializers
from models import User


class CreateUserSerializer(serializers.ModelSerializer):
    """
        User creation serializer
    """
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'username', 'pk')

        extra_kwargs = {
            'password': {'write_only': True},
            'pk': {'read_only': True}
        }

    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError("Minimum password length is 8 characters")
        return password
