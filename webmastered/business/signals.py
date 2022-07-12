from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings

from sendgrid import Mail, SendGridAPIClient

from .models import Staff, ServerUpgrade, Client
from dashboard.models import WebsiteSettings


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        Staff.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    pass


@receiver(post_save, sender=ServerUpgrade)
def server_upgrade_request_creation(sender, instance, created, **kwargs):
    if created:
        sendgrid = SendGridAPIClient(settings.SENDGRID_API_KEY)
        client_email = instance.user.email
        from_email = settings.DEFAULT_FROM_EMAIL
        wm_email = WebsiteSettings.objects.all()[0].business_email

        msg_client = Mail(
            from_email=from_email,
            to_emails=client_email,
        )
        msg_client.dynamic_template_data = {
            "username": str(instance.user.first_name),
        }
        msg_client.template_id = "d-fba4e1e4199f4340a44cc4042e720b23"

        msg_wm = Mail(
            from_email=from_email,
            to_emails=wm_email,
        )
        msg_wm.dynamic_template_data = {
            "username": str(instance.user.first_name),
            "domain_name": str(Client.objects.get(user=instance.user).domain_name),
            "request_datetime": str(instance.request_datetime.strftime("%a, %d-%b-%Y - %H:%M:%S %Z")),
            "comments": str(instance.comments),
        }
        msg_wm.template_id = "d-cbed40373145492ab5ad5a99f4fe600c"

        if not settings.DEBUG:
            sendgrid.send(msg_client)
            sendgrid.send(msg_wm)
