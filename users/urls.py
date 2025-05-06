from django.urls import path
from django.views.decorators.cache import never_cache
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserListApiView, UserCreateApiView, UserUpdateAPIView, UserDestroyApiView, UserRetrieveAPIView

app_name = UsersConfig.name

urlpatterns = [

    path('', UserListApiView.as_view(),name='users_list'),
    path('create/', UserCreateApiView.as_view(),name='user_create'),
    path('<int:pk>/update/', never_cache(UserUpdateAPIView.as_view()),name='user_update'),
    path('<int:pk>/delete/', UserDestroyApiView.as_view(),name='user_delete'),
    path('<int:pk>/detail/', UserRetrieveAPIView.as_view(),name='user_detail'),

    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),name='token_refresh')
]
