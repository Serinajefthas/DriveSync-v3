# Translates models into python format then converted into 
# easier rendered types; json, xml etc
from rest_framework import serializers
from models.user import User

class UserSerializer(serializers.ModelSerializer):
    """Converts user object into python format"""
    class Meta:
        model = User
        fields = ('user_id', 'firstName', 'lastName', 'email', 'phone')

class CreateUserSerializer(serializers.ModelSerializer):
    """Uses POST http method to create new user and serialize it"""
    class Meta:
        model = User
        fields = ('user_id', 'firstName', 'lastName', 'email', 'phone')
