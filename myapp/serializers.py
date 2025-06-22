from rest_framework import serializers
from django.contrib.auth.models import User
from myapp.models import TelegramUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ['id', 'user', 'telegram_username']