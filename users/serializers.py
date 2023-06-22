from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = '__all__'
        read_only_field = ['id']
        extra_kwargs = {"password": {"write_only": True}}

