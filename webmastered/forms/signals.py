from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from sendgrid import Mail, SendGridAPIClient

from forms.models import Contact
from dashboard.models import WebsiteSettings


@receiver(post_save, sender=Contact)
def new_contact_submission(sender, instance, created, **kwargs):
    if created:
        sendgrid = SendGridAPIClient(settings.SENDGRID_API_KEY)
        from_email = settings.DEFAULT_FROM_EMAIL
        wm_email = WebsiteSettings.objects.all()[0].business_email

        msg_wm = Mail(
            from_email=from_email,
            to_emails=wm_email,
        )
        msg_wm.dynamic_template_data = {
            "name": str(instance.name),
            "email": str(instance.email),
            "message": str(instance.message),
            "submitted": str(instance.submitted.strftime("%a, %d-%b-%Y - %H:%M:%S %Z")),
        }
        msg_wm.template_id = "d-47239f9665ff4d49ba7fc2a2064ffa24"

        if not settings.DEBUG:
            sendgrid.send(msg_wm)
