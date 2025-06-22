from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import *
from .tasks import send_mail  


@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def list_users(request):
 
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not password:
        return Response(
            {'error': 'Username and password are required.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(username=username).exists():
        return Response(
            {'error': 'Username already exists.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(username=username, email=email, password=password)


    if email:
        send_mail.delay(email,username)

    return Response(
        {'message': 'User created successfully'},
        status=status.HTTP_201_CREATED
    )

@api_view(['GET'])
@permission_classes([AllowAny])  
def list_telegram_users(request):
    """
    List all Telegram usernames stored in DB.
    Requires JWT auth.
    """
    telegram_users = TelegramUser.objects.all()
    serializer = TelegramUserSerializer(telegram_users, many=True)
    return Response(serializer.data)