from django import template
from django.template.loader import render_to_string
from django.conf import settings

from wagtail.rich_text import RichText, expand_db_html

from datetime import datetime

from home.models import HomePage
from dashboard.models import ModalMenuMainSectionPages, ModalMenuSubSectionPages, SocialMediaAccount

register = template.Library()


@register.simple_tag
def wm_richtext(value, content_tag, classes):
    if isinstance(value, RichText):
        # passing a RichText value through the |richtext filter should have no effect
        html = str(value)
        html = html.replace("<p", "<" + content_tag + " class=\"" + classes + "\"").replace("p>", content_tag + ">")
        # return render_to_string("wagtailcore/shared/richtext.html", {"html": html})
    elif value is None:
        html = ""
    else:
        if isinstance(value, str):
            html = expand_db_html(value)
            html = html.replace("<p", "<" + content_tag + " class=\"" + classes + "\"").replace("p>", content_tag + ">")
        else:
            raise TypeError(
                "'richtext' template filter received an invalid value; expected string, got {}.".format(
                    type(value)
                )
            )
    return render_to_string("wagtailcore/shared/richtext.html", {"html": html})


@register.simple_tag
def get_homepage():
    return HomePage.objects.all()[0]


@register.simple_tag
def get_modalnav_main():
    pages = []
    for item in ModalMenuMainSectionPages.objects.all():
        if item.page.live and item.page.show_in_menus:
            pages.append(item.page)
    return pages


@register.simple_tag
def get_modalnav_sub():
    pages = []
    for item in ModalMenuSubSectionPages.objects.all():
        if item.page.live and item.page.show_in_menus:
            pages.append(item.page)
    return pages


@register.simple_tag
def get_social_media_account():
    accounts = []
    for account in SocialMediaAccount.objects.all():
        accounts.append(account)
    return accounts


@register.simple_tag
def epoch_to_datetime(epoch):
    try:
        return datetime.fromtimestamp(epoch)
    except:
        return "ERROR!"


@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")