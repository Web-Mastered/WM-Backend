from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from forms.models import Contact
from forms.permission import ReadOnlyPermissionHelper


class ContactFormAdmin(ModelAdmin):
    model = Contact
    menu_label = "Contact Form"
    menu_icon = "inbox"
    list_display = ('name', 'email', 'submitted')
    list_export = ('name', 'email', 'message', 'submitted')
    export_filename = 'contact_form_submissions'
    list_filter = ('name', 'email', 'submitted')
    search_fields = ('name', 'email', 'message', 'submitted')
    permission_helper_class = ReadOnlyPermissionHelper
    inspect_view_enabled = True
    index_view_extra_js = ['js/engine/remove_edit_title_link_index_view.js', ]


class FormsAdminGroup(ModelAdminGroup):
    menu_label = 'Forms'
    menu_icon = "inbox"
    items = (ContactFormAdmin,)


modeladmin_register(FormsAdminGroup)
