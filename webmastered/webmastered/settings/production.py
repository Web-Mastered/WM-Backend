from .base import *
from webmastered import VERSION

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[
        DjangoIntegration(),
    ],
    traces_sample_rate=SENTRY_PRD_TRACE_SAMPLE_RATE,
    send_default_pii=True,
    release=VERSION,
    environment="production",
    debug=False,
)

try:
    from .local import *
except ImportError:
    pass
