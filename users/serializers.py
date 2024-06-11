from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_active=False
        )
        return user

class UserConfirmationSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()

    def validate(self, data):
        try:
            user = User.objects.get(username=data['username'])
            if user.confirmation_code != data['confirmation_code']:
                raise serializers.ValidationError("Invalid confirmation code.")
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist.")
        return data