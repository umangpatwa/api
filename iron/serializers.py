# from django.contrib.auth.models import User, Group
# from uuid import uuid4
from rest_framework import serializers
# from rest_framework.fields import CurrentUserDefault
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
# from allauth.account.adapter import get_adapter
# from allauth.account import app_settings as allauth_settings
# from allauth.utils import email_address_exists, get_username_max_length
from .models import User


class CustomRegisterSerializer(RegisterSerializer):
    """Use default serializer except don't user username"""
    username = None

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def get_cleaned_data(self):
        return {
            "password1": self.validated_data.get("password1", ""),
            "email": self.validated_data.get("email", ""),
        }


class CustomLoginSerializer(LoginSerializer):
    """Use default serializer except don't user username"""

    username = None

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'is_superuser']
