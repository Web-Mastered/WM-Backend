from django.utils.html import format_html
from django.templatetags.static import static

from wagtail import hooks
from wagtail.admin.views.account import BaseSettingsPanel

from .forms import CustomStaffSettingsForm


@hooks.register('insert_global_admin_css')
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{}">', static('css/engine.css'))

@hooks.register('register_account_settings_panel')
class CustomStaffSettingsPanel(BaseSettingsPanel):
    name = 'custom_staff'
    title = "Staff settings"
    order = 300
    form_class = CustomStaffSettingsForm
    form_object = 'profile'

    def get_form(self):
        """
        Returns an initialised form.
        """
        kwargs = {
            'instance': self.request.user.staff_profile,
            'prefix': self.name
        }

        if self.request.method == 'POST':
            return self.form_class(self.request.POST, **kwargs)
        else:
            return self.form_class(**kwargs)


@hooks.register('register_icons')
def wm_engine_ui_icons(icons):
    for icon in [
        'briefcase.svg',
        'server.svg',
        'inbox.svg',
        'heading.svg',
        'table-columns.svg',
        'sterling-sign.svg',
        'timeline.svg',
    ]:
        icons.append('engine/icons/{}'.format(icon))
    return icons


