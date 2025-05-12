from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView , DestroyAPIView , RetrieveAPIView, UpdateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated , AllowAny
# Create your views here.

from users.serializers.user_serializers import UserCreateSerializer, UserUpdateSerializer , UserSerializer ,UserTokenObtainPairSerializer
from users.models import  User

class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)

class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = (AllowAny,)

    #
    # def get_queryset(self):
    #     user = self.request.user
    #     return User.objects.filter(id=user.id)

class UserDestroyApiView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer




