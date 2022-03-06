from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = User
        fields = ("__all__")