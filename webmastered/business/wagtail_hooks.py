from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from business.models import Client, Staff, ServerUpgrade, StaffRoles


class StaffRolesAdmin(ModelAdmin):
    model = StaffRoles
    menu_label = "Staff Roles"
    menu_icon = "group"


class ServerUpgradeAdmin(ModelAdmin):
    model = ServerUpgrade
    menu_label = "Server Upgrade"
    menu_icon = "server"
    list_display = ('__str__', 'client', 'request_datetime', 'report_submitted', 'scheduled_datetime', 'is_finished')
    search_fields = (
        '__str__',
        'client',
        'comments',
        'request_datetime',
        'report_submitted',
        'scheduled_datetime',
        'is_finished'
    )
    inspect_view_enabled = True
    index_view_extra_js = ['js/engine/remove_edit_title_link_index_view.js', ]


class ClientAdmin(ModelAdmin):
    model = Client
    menu_label = "Clients"
    menu_icon = "user"
    list_display = ('__str__', 'company_name', 'domain_name', 'email_address')
    list_export = (
        '__str__',
        'email_address',
        'company_name',
        'domain_name',
        'stripe_customer_id',
        'cloudflare_zone_id',
        'digitalocean_droplet_id'

    )
    export_filename = 'clients_list'
    search_fields = (
        '__str__',
        'email_address',
        'company_name',
        'domain_name',
        'stripe_customer_id',
        'cloudflare_zone_id',
        'digitalocean_droplet_id'

    )
    inspect_view_enabled = True
    index_view_extra_js = ['js/engine/remove_edit_title_link_index_view.js', ]


class StaffAdmin(ModelAdmin):
    model = Staff
    menu_label = "Staff"
    menu_icon = "user"


class WMBusinessAdminGroup(ModelAdminGroup):
    menu_label = 'WM Business'
    menu_icon = "briefcase"
    items = (StaffRolesAdmin, StaffAdmin, ClientAdmin, ServerUpgradeAdmin)


modeladmin_register(WMBusinessAdminGroup)
