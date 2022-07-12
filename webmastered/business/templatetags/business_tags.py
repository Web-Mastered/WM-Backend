from django import template

from business.models import Staff

register = template.Library()


@register.simple_tag
def get_staff_list():
    """returns the staff models"""
    staff = Staff.objects.all()
    return staff
