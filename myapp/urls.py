from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', register_user),  #public api 
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #protected api
    path('users/', list_users), #Private api required Authentication Access
    path('telegram-users/', list_telegram_users) #to see the telegram user stored in data base
]
