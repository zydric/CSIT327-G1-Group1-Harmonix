from rest_framework import serializers
from .models import User
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Include all editable fields
        fields = [
            'username', 'email', 'role',
            'location', 'genres', 'instruments'
        ]
        extra_kwargs = {
            'email': {'read_only': True}, #Prevents users changing their role
            'username': {'required': False},
            'role': {'read_only': True}, #Prevents users changing their role
            'location': {'required': False},
            'genres': {'required': False},
            'instruments': {'required': False},
        }
