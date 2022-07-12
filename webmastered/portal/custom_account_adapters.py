from allauth.account.adapter import DefaultAccountAdapter

from django.conf import settings
from django.contrib import messages

from sendgrid import Mail, SendGridAPIClient


class WMPortalAccountAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request):
        """
        Checks whether or not the site is open for signups.

        Next to simply returning True/False you can also intervene the
        regular flow by raising an ImmediateHttpResponse

        (Comment reproduced from the overridden method.)
        """
        return False

    def get_email_confirm_expire_days_pretty(self):
        days = settings.ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS
        if days > 1:
            return str(days) + " days"
        else:
            return str(days) + " day"

    def get_pass_reset_expire_days_pretty(self):
        days = settings.PASSWORD_RESET_TIMEOUT / 86400
        if days > 1:
            return str(days) + " days"
        else:
            return str(days) + " day"

    def render_mail(self, template_prefix, email, context, headers=None):
        """
        Renders an e-mail to `email`.  `template_prefix` identifies the
        e-mail that is to be sent, e.g. "account/email/email_confirmation"

        Overridden to support SendGrid's Dynamic Templates.
        """
        to = [email] if isinstance(email, str) else email

        from_email = self.get_from_email()

        msg = Mail(
            from_email=from_email,
            to_emails=to,
        )

        this_email_job = str(template_prefix).replace("account/email/", "")
        match this_email_job:
            case "email_confirmation":
                msg.dynamic_template_data = {
                    "username": str(context['user'].first_name),
                    "activation_link": str(context['activate_url']),
                    "activation_validity": self.get_email_confirm_expire_days_pretty(),
                }
                msg.template_id = "d-24a5dfdcb4274eb1844b037cff42178d"

            case "password_reset_key":
                msg.dynamic_template_data = {
                    "username": str(context['user'].first_name),
                    "reset_link": str(context['password_reset_url']),
                    "reset_validity": self.get_pass_reset_expire_days_pretty(),
                }
                msg.template_id = "d-fff7024cd8ba4e02878e266855ed9db2"

        return msg

    def send_mail(self, template_prefix, email, context):
        msg = self.render_mail(template_prefix, email, context)
        sendgrid = SendGridAPIClient(settings.SENDGRID_API_KEY)
        if settings.DEBUG:
            messages.add_message(self.request, messages.ERROR, 'Email not sent - Engine CMS in debug mode')
        else:
            sendgrid.send(msg)
