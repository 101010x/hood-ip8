from rest_framework import serializers
from .models import User, Post, Profile, Hood, EmergencyService, Bussiness
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    '''Serializer for user Model'''
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password')
    
    def validate_password(self, value: str) -> str:
        return make_password(value)

class HoodSerializer(serializers.ModelSerializer):
    '''Serializer for Hood Model'''
    admin = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Hood
        exclude = ['id','occupants_count']

class ProfileSerializer(serializers.ModelSerializer):
    '''Serializer for profile Model'''
    user = serializers.StringRelatedField(read_only=True)
    hood = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Profile
        exclude = ['id']

class PostSerializer(serializers.ModelSerializer):
    '''Serializer for Post Model'''
    user = serializers.StringRelatedField(read_only=True)
    hood = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Post
        exclude = ['id', 'pub_date']

class BussinessSerializer(serializers.ModelSerializer):
    '''Serializer for Bussiness class'''
    hood = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Bussiness
        exclude = ['id']


class EmergencyServiceSerializer(serializers.ModelSerializer):
    '''Serializer for Bussiness class'''
    hood = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = EmergencyService
        exclude = ['id']