"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.14.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from datetime import timedelta
from pathlib import Path
import os

from django.conf.global_settings import  CACHES, CSRF_TRUSTED_ORIGINS
from django.core.cache import cache
from dotenv import load_dotenv
load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=kz!r1-!(#)5+vtx=@^lr6j2)gn$4ofi5$w-nas8qkm%p$@bp7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    #base apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # installed apps
    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt',
    'corsheaders',
    'drf_yasg',
    'redis',
    #my apps
    'users',
    'sections',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# local SSMS
# DRIVER = os.getenv('MS_SQL_DRIVER')
# HOST = os.getenv('MS_SQL_SERVER')
# DATABASE = os.getenv('MS_SQL_DATABASE')
# USER = os.getenv('MS_SQL_USER')
# PASSWORD = os.getenv('MS_SQL_KEY')
# PAD_DATABASE = os.getenv('MS_PAD_DATA_BASE')


# DATABASES = {
#     'default': {
#         'ENGINE': 'mssql',
#         'NAME': DATABASE,
#         'USER': USER,
#         'PASSWORD':PASSWORD,
#         'HOST':HOST,
#         'PORT':'',
#         'OPTIONS':
#                 {
#                 'driver':DRIVER,
#                 },
#     }
# }
#

#docker and postgres
# коментарий для преподавателя
# я вот не понял можно ли в докере
# как то сделать так чтобы он команды для запуска только один раз применял
# у меня получилось так что если я делаю в докере ccsu при установке базы
# он первый раз устанавливает нормально если база пустая
# а второй раз он вылетает с ошибкой типо пользователи созданы
# в целом можно навреное в саму команду добавить обработку логики на такой случай чтобы она не
# создавала пользователей если они уже  созданы были
# но хотелось бы конечно как то через докер это сделать
# я вот искал гуглил ничего не нашел поэтому поводу как имено один раз это сделать
# у меня решилось через фикстуры я просто фикстуры загружаю каждый раз и ошибки нет никакой
# но суть в том что при каждой перезагрузке в docker Dekstop так происходит фикстуры грузятся
# может вы знаете как этого избежать ?
# ну или может у вас  ссылка есть на статью где описано как это решить
database_name =os.getenv('POSTGRESQL_DATABASE_DOCKER')
database_user = os.getenv('POSTGRESQL_USER')
database_password = os.getenv('POSTGRESQL_PASSWORD_DOCKER')
database_port = os.getenv('POSTGRESQL_PORT_DOCKER')
doker_host = os.getenv('POSTGRESQL_HOST_DOCKER')
local_host = os.getenv('POSTGRESQL_HOST')
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
        'NAME': database_name,
        'USER': database_user,
        'PASSWORD':database_password,
        'HOST':doker_host, # для докера
        # 'HOST': local_host, для локального подключения
        'PORT':database_port,

    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (
    BASE_DIR / 'static',
)
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

cache_status = os.getenv('CACHE_ENABLED')
CACHE_ENABLED = cache_status

if CACHE_ENABLED:
    CACHES = {
        'default' :{
            "BACKEND":"django.core.cache.backends.redis.RedisCache",
            "LOCATION":os.getenv('CACHE_LOCATION')
        }
    }

#
REST_FRAMEWORK ={
    'DEFAULT_FILTER_BACKENDS':['django_filters.rest_framework.DjangoFilterBackend',],
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework_simplejwt.authentication.JWTAuthentication',],
    'DEFAULT_PERMISSION_CLASSES':['rest_framework.permissions.IsAuthenticated',],
    # 'DEFAULT_PERMISSION_CLASSES':['rest_framework.permissions.AllowAny',],
    'TEST_REQUEST_DEFAULT_FORMAT':'json',
    # 'TEST_REQUEST_RENDERER_CLASSES':[
    #     'rest_framework.renderers.MultiPartRenderer',
    #     'rest_framework.renderers.JSONRenderer',
    #     'rest_framework.renderers.TemplateHTMLRenderer',
    # ]
}

SIMPLE_JWT ={
    'ACCESS_TOKEN_LIFETIME':timedelta(minutes=180),
    'REFRESH_TOKEN_LIFETIME':timedelta(days=7),
}

CORS_ALLOWED_ORIGINS =[
    'http://read-only.example.com',
    'http://read-and-write.example.com'
]

CSRF_TRUSTED_ORIGINS=[
    'http://read-and-write.example.com'
]