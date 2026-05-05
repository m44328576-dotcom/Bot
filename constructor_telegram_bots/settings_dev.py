from django.utils.translation import gettext_lazy as _

import django_stubs_ext

from datetime import timedelta
from pathlib import Path
from typing import Any, Final
import os
import sys

django_stubs_ext.monkeypatch()


BASE_DIR: Final[Path] = Path(__file__).resolve().parent.parent
LOGS_DIR: Final[Path] = BASE_DIR / 'logs'

os.makedirs(LOGS_DIR, exist_ok=True)


SECRET_KEY: Final[str] = os.environ.get('SECRET_KEY', 'dev-secret-key-not-for-production-12345')

TEST: Final[bool] = bool(len(sys.argv) >= 2 and sys.argv[1] == 'test')
DEBUG: Final[bool] = True
ENABLE_TELEGRAM_AUTH: Final[bool] = False

TELEGRAM_BOT_TOKEN: Final[str] = os.environ.get('TELEGRAM_BOT_TOKEN', 'dummy-token')

FRONTEND_PATH: Final[Path] = Path(os.environ.get('FRONTEND_PATH', str(BASE_DIR / 'frontend')))


ALLOWED_HOSTS: Final[list[str]] = ['*']
CSRF_TRUSTED_ORIGINS: Final[list[str]] = ['https://*.exg1o.org', 'http://localhost:*', 'http://127.0.0.1:*']


CSRF_COOKIE_AGE: Final[int] = 2419200  # 4 weeks
SESSION_COOKIE_AGE: Final[int] = 2419200  # 4 weeks

FILE_UPLOAD_MAX_MEMORY_SIZE: Final[int] = 62914560  # 60M

TELEGRAM_BOT_MAX_TRIGGERS: Final[int] = 250
TELEGRAM_BOT_MAX_MESSAGES: Final[int] = 500
TELEGRAM_BOT_MAX_MESSAGE_KEYBOARD_BUTTONS: Final[int] = 100
TELEGRAM_BOT_MAX_CONDITIONS: Final[int] = 750
TELEGRAM_BOT_MAX_CONDITION_PARTS: Final[int] = 25
TELEGRAM_BOT_MAX_BACKGROUND_TASKS: Final[int] = 25
TELEGRAM_BOT_MAX_API_REQUESTS: Final[int] = 100
TELEGRAM_BOT_MAX_DATABASE_OPERATIONS: Final[int] = 250
TELEGRAM_BOT_MAX_INVOICES: Final[int] = 250
TELEGRAM_BOT_MAX_INVOICE_PRICES: Final[int] = 1
TELEGRAM_BOT_MAX_TEMPORARY_VARIABLES: Final[int] = 1000
TELEGRAM_BOT_MAX_VARIABLES: Final[int] = 100
TELEGRAM_BOT_MAX_DATABASE_RECORDS: Final[int] = 1000


JWT_REFRESH_TOKEN_LIFETIME: Final[timedelta] = timedelta(weeks=4)
JWT_ACCESS_TOKEN_LIFETIME: Final[timedelta] = timedelta(minutes=15)


# Disable Celery for development (use dummy backend)
CELERY_BROKER_URL: Final[str] = 'memory://'
CELERY_RESULT_BACKEND: Final[str] = 'cache+memory://'
CELERY_ACCEPT_CONTENT: Final[list[str]] = ['application/json']
CELERY_RESULT_SERIALIZER: Final[str] = 'json'
CELERY_TASK_SERIALIZER: Final[str] = 'json'
CELERY_TASK_ALWAYS_EAGER: Final[bool] = True  # Run tasks synchronously
CELERY_BEAT_SCHEDULE: Final[dict[str, dict[str, Any]]] = {}


INSTALLED_APPS: Final[list[str]] = [
    'rest_framework',
    'django_filters',
    'drf_standardized_errors',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'adminsortable2',
    'languages',
    'users',
    'telegram_bots',
    'telegram_bots.hub',
    'instruction',
    'donation',
    'privacy_policy',
    'terms_of_service',
]

REST_FRAMEWORK: Final[dict[str, Any]] = {
    'EXCEPTION_HANDLER': 'drf_standardized_errors.handler.exception_handler'
}


MIDDLEWARE: Final[list[str]] = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]


TEMPLATES: Final[list[dict[str, Any]]] = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates', FRONTEND_PATH / 'dist'],
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

AUTHENTICATION_BACKENDS: Final[list[str]] = ['django.contrib.auth.backends.ModelBackend']

AUTH_USER_MODEL: Final[str] = 'users.User'
ROOT_URLCONF: Final[str] = 'constructor_telegram_bots.urls'
WSGI_APPLICATION: Final[str] = 'constructor_telegram_bots.wsgi.application'


# Use local memory cache instead of Redis
CACHES: Final[dict[str, dict[str, Any]]] = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}


# Use SQLite instead of PostgreSQL for development
DATABASES: Final[dict[str, dict[str, Any]]] = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}
DEFAULT_AUTO_FIELD: Final[str] = 'django.db.models.BigAutoField'


USE_I18N: Final[bool] = True
USE_L10N: Final[bool] = True

LANGUAGE_COOKIE_NAME: Final[str] = 'lang'

LANGUAGES: Final[list[tuple[str, Any]]] = [
    ('en', _('Английский')),
    ('uk', _('Украинский')),
    ('ru', _('Русский')),
]
LANGUAGE_CODE: Final[str] = 'ru-ru'
MODELTRANSLATION_DEFAULT_LANGUAGE: Final[str] = 'ru'
LOCALE_PATHS: Final[list[Path]] = [BASE_DIR / 'locale']


TIME_ZONE: Final[str] = 'UTC'
USE_TZ: Final[bool] = True


STATIC_URL: Final[str] = '/static/'
STATIC_ROOT: Final[Path] = BASE_DIR / 'static'
STATICFILES_DIRS: Final[list[Path | str]] = []

MEDIA_URL: Final[str] = '/media/'
MEDIA_ROOT: Final[Path] = BASE_DIR / 'media'


LOGGING: Final[dict[str, Any]] = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{asctime}]: {levelname}: {name} > {funcName} || {message}',
            'style': '{',
        },
        'simple': {
            'format': '[{asctime}]: {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
    },
}
