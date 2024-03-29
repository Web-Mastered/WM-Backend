from .base import *
from webmastered import VERSION

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.redis import RedisIntegration

if os.environ.get('DEBUG') == 'False':
    DEBUG = False
else:
    DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['http://localhost:1337']

if os.environ.get('FULL_URL'):
    CSRF_TRUSTED_ORIGINS.append(os.environ.get('FULL_URL'))

WAGTAILADMIN_BASE_URL = os.environ.get('FULL_URL')

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
DIGITALOCEAN_ACCESS_TOKEN = os.environ.get('DIGITALOCEAN_ACCESS_TOKEN')
CLOUDFLARE_API_TOKEN = os.environ.get('CLOUDFLARE_API_TOKEN')
STRIPE_API_KEY = os.environ.get('STRIPE_API_KEY')
SENTRY_DSN = os.environ.get('SENTRY_DSN')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[
        DjangoIntegration(),
        RedisIntegration(),
    ],
    traces_sample_rate=SENTRY_PRD_TRACE_SAMPLE_RATE,
    send_default_pii=True,
    release=VERSION,
    environment="production",
    debug=False,
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': 5432,
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis/db_engine',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PASSWORD': os.environ.get('REDIS_PASSWORD')
        }
    }
}


try:
    from .local import *
except ImportError:
    pass
