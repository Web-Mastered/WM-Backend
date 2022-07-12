from django import template

from portal import VERSION as portal_version
from business.models import Client

register = template.Library()


@register.simple_tag()
def client_portal_version():
    return portal_version


@register.simple_tag(takes_context=True)
def get_client_company_name(context):
    request = context['request']
    company_name = Client.objects.get(user=request.user).company_name
    return company_name
