import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'you_need_to_set_the_secret_key_in_env')

DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost, 127.0.0.1').split(', ')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'django_filters',

    'corsheaders',

    'users.apps.UsersConfig',
    'recipes.apps.RecipesConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'foodgram.urls'

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

WSGI_APPLICATION = 'foodgram.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'django'),
        'USER': os.getenv('POSTGRES_USER', 'django'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', ''),
        'PORT': os.getenv('DB_PORT', 5432)
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.sqlite3'),
#         'NAME': os.environ.get('SQL_DATABASE', BASE_DIR / 'db.sqlite3'),
#         'USER': os.environ.get('SQL_USER', 'user'),
#         'PASSWORD': os.environ.get('SQL_PASSWORD', 'password'),
#         'HOST': os.environ.get('SQL_HOST', 'localhost'),
#         'PORT': os.environ.get('SQL_PORT', '5432'),
#     }
# }

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


CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = os.getenv('TIME_ZONE', default='')

USE_I18N = True

USE_L10N = True

USE_TZ = os.getenv('USE_TZ', 'True') == 'True'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'collected_static'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'

DJOSER = {
    'LOGIN_FIELD': 'email',
    'HIDE_USERS': False,
    'SERIALIZERS': {
        'user': 'users.serializers.CustomUserSerializer',
        'user_create': 'users.serializers.CustomCreateUserSerializer',
        'current_user': 'users.serializers.CustomUserSerializer',
    },
    'PERMISSIONS': {
        'user': ['djoser.permissions.CurrentUserOrAdminOrReadOnly'],
        'user_list': ['rest_framework.permissions.AllowAny']
    },
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication'
    ],

    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ]
}

CSV_DIR = os.path.join(BASE_DIR, 'data')

INGREDIENT_NAME_MAX_LENGTH = 200
INGREDIENT_UNIT_OF_MEASUREMENT_MAX_LENGTH = 200

TAG_NAME_MAX_LENGTH = 50
TAG_SLUG_MAX_LENGTH = 200
TAG_COLOR_MAX_LENGTH = 7

RECIPE_NAME_MAX_LENGTH = 200

CUSTOM_USER_EMAIL_MAX_LENGTH = 254
CUSTOM_USER_USERNAME_MAX_LENGTH = 150
CUSTOM_USER_FIRST_NAME_MAX_LENGTH = 150
CUSTOM_USER_LAST_NAME_MAX_LENGTH = 150
CUSTOM_USER_PASSWORD_MAX_LENGTH = 150
