from django.conf import settings
from django import template
from django.utils.safestring import mark_safe

import webmastered

register = template.Library()


@register.simple_tag()
def generate_plausible_js():
    url = settings.WAGTAILADMIN_BASE_URL
    domain = url.replace("https://www.", "")
    return mark_safe(f'<script defer data-domain="{domain}" src="https://analytics.{domain}/js/plausible.js"></script>')


@register.simple_tag()
def generate_sentry_js():
    script_src = "https://browser.sentry-cdn.com/7.6.0/bundle.tracing.min.js"
    script_integrity = "sha384-Xq/3Nmu7NlebKM710GahhIbqq6na6mHcKZZl4nrO9wnfETcVVTfZVGGzz1xzxxxC"
    js = f'<script src="{script_src}" integrity="{script_integrity}" crossorigin="anonymous"></script>'

    if settings.DEBUG:
        environment = "development"
        sampleRate = settings.SENTRY_DEV_TRACE_SAMPLE_RATE
    else:
        environment = "production"
        sampleRate = settings.SENTRY_PRD_TRACE_SAMPLE_RATE

    init = """<script>
    Sentry.init({
        dsn: "%s",
        debug: %s,
        release: "%s",
        environment: "%s",
        sampleRate: %s,
        integrations: [new Sentry.BrowserTracing()],
    })</script>
    """ % (
        settings.SENTRY_DSN,
        str(settings.DEBUG).lower(),
        webmastered.VERSION,
        environment,
        sampleRate
    )

    return mark_safe(js + "\n" + init)
