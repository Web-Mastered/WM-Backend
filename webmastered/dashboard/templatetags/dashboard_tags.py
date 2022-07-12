from wagtail.admin.search import admin_search_areas
from wagtail.admin.ui import sidebar
from wagtail.admin.menu import admin_menu
from wagtail.telepath import JSContext

from django import template
from django.urls import reverse
from django.utils.html import json_script
from django.utils.translation import gettext_lazy as _

from webmastered import VERSION as engine_version
from webmastered import CLIENT as client

register = template.Library()


@register.simple_tag(takes_context=True)
def wm_sidebar_props(context):
    request = context["request"]
    search_areas = admin_search_areas.search_items_for_request(request)
    if search_areas:
        search_area = search_areas[0]
    else:
        search_area = None

    account_menu = [
        sidebar.LinkMenuItem(
            "account", _("Account"), reverse("wagtailadmin_account"), icon_name="user"
        ),
        sidebar.LinkMenuItem(
            "logout", _("Log out"), reverse("wagtailadmin_logout"), icon_name="logout"
        ),
    ]

    modules = [
        sidebar.WagtailBrandingModule(),
        sidebar.SearchModule(search_area) if search_area else None,
        sidebar.MainMenuModule(
            admin_menu.render_component(request), account_menu, request.user
        ),
    ]
    modules = [module for module in modules if module is not None]

    json_one = JSContext().pack(modules)
    for item_one in json_one:
        if item_one.get("_type") == "wagtail.sidebar.MainMenuModule":
            json_two = item_one.get("_args")
            for list in json_two:
                for item_two in list:
                    try:
                        if item_two.get("_type") == "wagtail.sidebar.SubMenuItem":
                            for parameters in item_two.get("_args"):
                                try:
                                    if parameters.get('name') == "settings":
                                        parameters['footer_text'] = client + "\nEngine CMS v" + engine_version
                                except:
                                    pass
                    except:
                        pass

    json_output = json_script(
        {
            "modules": json_one,
        },
        element_id="wagtail-sidebar-props",
    )

    return json_output

