from allauth.account.forms import LoginForm, ResetPasswordForm, AddEmailForm, ChangePasswordForm

from django.contrib import messages

import json


class WMPortalLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(WMPortalLoginForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            default_classes = [
                "font-paragraph",
            ]
            match field.widget.input_type:
                case "text":
                    classes = default_classes
                    classes.append("form-input w-full border-0 border-b-2 focus:ring-0 focus:border-wm-blue")
                    field.widget.attrs.update({
                        'class': " ".join(classes)
                    })
                case "password":
                    classes = default_classes
                    classes.append("form-input w-full border-0 border-b-2 focus:ring-0 focus:border-wm-blue")
                    field.widget.attrs.update({
                        'class': " ".join(classes)
                    })
                case "checkbox":
                    classes = default_classes
                    classes.append("form-checkbox")
                    field.widget.attrs.update({
                        'class': " ".join(classes)
                    })
        try:
            messages.add_message(self.request, messages.ERROR,
                                 json.loads(self.errors.as_json())["__all__"][0]["message"])
        except:
            pass

    def login(self, *args, **kwargs):
        # You must return the original result.
        return super(WMPortalLoginForm, self).login(*args, **kwargs)


class WMPortalPasswordResetForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(WMPortalPasswordResetForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            default_classes = [
                "font-paragraph",
            ]
            match field.widget.input_type:
                case "email":
                    classes = default_classes
                    classes.append("form-input")
                    field.widget.attrs.update({
                        'class': " ".join(classes)
                    })
        try:
            messages.add_message(self.request, messages.ERROR,
                                 json.loads(self.errors.as_json())["__all__"][0]["message"])
        except:
            pass

    def _send_unknown_account_mail(self, request, email):
        messages.add_message(request, messages.ERROR, "A reset link has not been sent as this email is not registered "
                                                      "with an account. Please go back and correct the entry.")


class WMPortalAddEmailForm(AddEmailForm):
    def __init__(self, *args, **kwargs):
        super(WMPortalAddEmailForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            default_classes = [
                "font-paragraph",
            ]
            match field.widget.input_type:
                case "email":
                    classes = default_classes
                    classes.append("form-input")
                    field.widget.attrs.update({
                        'class': " ".join(classes)
                    })
        try:
            messages.add_message(self.request, messages.ERROR,
                                 json.loads(self.errors.as_json())["__all__"][0]["message"])
        except:
            pass


class WMPortalChangePasswordForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super(WMPortalChangePasswordForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            default_classes = [
                "font-paragraph",
            ]
            match field.widget.input_type:
                case "password":
                    classes = default_classes
                    classes.append("form-input")
                    field.widget.attrs.update({
                        'class': " ".join(classes)
                    })
