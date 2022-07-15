from django.db import models
from django.contrib.auth.models import User

from wagtail.admin.panels import FieldPanel

from datetime import datetime


class StaffRoles(models.Model):
    role = models.CharField(max_length=100, unique=True,
                            help_text="Create new staff roles here, these roles an be assigned to 'staff' users.")
    panels = [
        FieldPanel('role'),
    ]

    def __str__(self):
        return self.role

    class Meta:
        verbose_name = "Staff Role"
        verbose_name_plural = "Staff Roles"


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="staff_profile")
    roles = models.ManyToManyField(StaffRoles, blank=True,
                                   help_text="You can select multiple roles by doing CMD+Click or CTRL+Click")

    def __str__(self):
        if self.user.first_name:
            return str(self.user.first_name) + " " + str(self.user.last_name)
        else:
            return str(self.user.username)

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="client_profile")
    company_name = models.CharField(help_text="Customer's company name.", max_length=255, unique=False)
    domain_name = models.CharField(help_text="Customer's website domain name.", max_length=255, unique=False)
    stripe_customer_id = models.CharField(help_text="Stripe ID of customer", max_length=255, unique=False,
                                          verbose_name="Stripe Customer ID")
    cloudflare_zone_id = models.CharField(help_text="CF Zone ID of customer", max_length=255, unique=False,
                                          verbose_name="Cloudflare Zone ID")
    digitalocean_droplet_id = models.CharField(help_text="DO Droplet ID of customer", max_length=255, unique=False,
                                               verbose_name="DigitalOcean Droplet ID")

    def __str__(self):
        if self.user.first_name:
            return str(self.user.first_name) + " " + str(self.user.last_name)
        else:
            return str(self.user.username)

    def email_address(self):
        return self.user.email

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class ServerUpgrade(models.Model):
    # 1 - Client requests for a server upgrade
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    comments = models.TextField(
        max_length=500000,
        blank=True,
        null=True,
    )
    request_datetime = models.DateTimeField(
        auto_now_add=datetime.now()
    )
    # 2 - WM team monitors' server perf and creates a small report of what needs to be upgraded
    # 3 - When the report is submitted, this bool has to be set to true
    report_submitted = models.BooleanField()
    # 4 - An agreement of the upgrade, pricing and date time of when the upgrade should be carried out is made
    scheduled_datetime = models.DateTimeField(
        editable=True,
        blank=True,
        null=True,
    )
    # 5 - When the upgrade is finished, this is set to true
    is_finished = models.BooleanField()

    def __str__(self):
        return "Server Upgrade Request " + str(self.id)

    def client(self):
        if self.user.first_name:
            return str(self.user.first_name) + " " + str(self.user.last_name)
        else:
            return str(self.user.username)

    class Meta:
        verbose_name = "Server Upgrade Request"
        verbose_name_plural = "Server Upgrade Requests"
