from django.db import models
from django.contrib.auth.models import User

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.panels import FieldRowPanel, TabbedInterface, ObjectList, FieldPanel, PageChooserPanel, \
    MultiFieldPanel, InlinePanel, HelpPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.models import Orderable


class SocialMediaAccount(Orderable):
    SOCIAL_MEDIA_CHOICES = [
        ('fa-instagram', 'Instagram'),
        ('fa-linkedin', 'LinkedIn'),
        ('fa-facebook', 'Facebook'),
        ('fa-github', 'GitHub'),
    ]

    account = ParentalKey("WebsiteSettings", related_name="social_media_account", on_delete=models.CASCADE,
                          null=False, blank=False)

    account_platform = models.CharField(
        max_length=255,
        choices=SOCIAL_MEDIA_CHOICES,
        null=False,
        blank=False,
        help_text="Select the social media platform for this account.",
        verbose_name="Platform"
    )

    account_username = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        help_text="Enter the username for your account with this social media platform.",
        verbose_name="Username"
    )

    account_url = models.URLField(
        max_length=1024,
        null=False,
        blank=False,
        help_text="Enter the URL to your account for this social media platform.",
        verbose_name="Account URL"
    )


class ModalMenuMainSectionPages(Orderable):
    mainsect_page = ParentalKey("WebsiteSettings", related_name="modalmenu_mainsect_page", on_delete=models.CASCADE,
                                null=True, blank=True)
    page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Page",
        help_text="Set a page to display in the main section of the modal menu",
    )


class ModalMenuSubSectionPages(Orderable):
    subsect_page = ParentalKey("WebsiteSettings", related_name="modalmenu_subsect_page", on_delete=models.CASCADE,
                               null=True, blank=True)
    page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Page",
        help_text="Set a page to display in the sub section of the modal menu",
    )


@register_setting
class WebsiteSettings(BaseSetting, ClusterableModel):
    lightmode_logo = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text="Choose an image for this site's light mode logo. This logo will be displayed on light backgrounds."
    )

    darkmode_logo = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text="Choose an image for this site's dark mode logo. This logo will be displayed on dark backgrounds."
    )

    site_icon = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text="Site icons are what you see in browser tabs and bookmark bars, please upload a square image."
    )

    footer_text = RichTextField(
        blank=True,
        null=True,
        features=[
            'emphasis',
            'bold',
            'italic',
            'link',
            'document-link',
            'code',
            'superscript',
            'subscript',
            'strikethrough',
        ],
        verbose_name="Footer text",
        help_text="This text will be displayed below the logo in the footer.",
    )

    cookie_policy_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Cookie policy",
        help_text="Set your cookie policy page, this page will be listed in specific parts of the menus",
    )

    privacy_policy_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Privacy policy",
        help_text="Set your privacy policy page, this page will be listed in specific parts of the menus",
    )

    terms_and_conditions_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Terms & conditions",
        help_text="Set your terms & conditions page, this page will be listed in specific parts of the menus",
    )

    business_email = models.EmailField(
        max_length=254,
        null=True,
        blank=True,
        help_text="Enter the email address for this business"
    )

    company_legal_name = models.CharField(
        max_length=255,
        blank=True,
        null=False,
        verbose_name="Legal Business Name",
        help_text="Enter the legal name of the company"
    )

    company_name = models.CharField(
        max_length=255,
        blank=True,
        null=False,
        help_text="Enter the name of the company"
    )

    company_slogan = models.CharField(
        max_length=1000,
        blank=True,
        null=False,
        help_text="Enter the company slogan"
    )

    company_description = models.CharField(
        max_length=2000,
        blank=True,
        null=False,
        help_text="Enter the description for this company"
    )

    look_and_feel_panels = [
        MultiFieldPanel(
            [
                ImageChooserPanel("lightmode_logo"),
                ImageChooserPanel("darkmode_logo"),
                ImageChooserPanel("site_icon"),
            ],
            heading="Logos"
        ),
        MultiFieldPanel(
            [
                FieldPanel('footer_text'),
            ],
            heading="Footer"
        ),
        MultiFieldPanel(
            [
                HelpPanel(
                    content="""
                    
                    <div class="help-block help-info">
                        <svg class="icon icon-help icon" aria-hidden="true"><use href="#icon-help"></use></svg>
                        <p>
                            Add pages to be displayed in the main section of the modal menu (the menu that pops open
                            when the menu button is pressed by the user)
                        </p>
                    </div>
                    
                    """
                ),
                InlinePanel("modalmenu_mainsect_page", label="Main Section Pages"),
                HelpPanel(
                    content="""

                    <div class="help-block help-info">
                        <svg class="icon icon-help icon" aria-hidden="true"><use href="#icon-help"></use></svg>
                        <p>
                            Add pages to be displayed in the sub section of the modal menu (the menu that pops open
                            when the menu button is pressed by the user)
                        </p>
                    </div>
            
                    """
                ),
                InlinePanel("modalmenu_subsect_page", label="Sub Section Pages"),
            ],
            heading="Modal Menu"
        )

    ]

    legal_compliance_panels = [
        MultiFieldPanel(
            [
                FieldPanel("company_legal_name"),
                FieldPanel("company_name"),
            ],
            heading="Company Name",
            help_text="Set the name of your company."
        ),
        MultiFieldPanel(
            [
                PageChooserPanel('cookie_policy_page'),
                PageChooserPanel('privacy_policy_page'),
                PageChooserPanel('terms_and_conditions_page'),
            ],
            heading="Legal Pages",
            help_text="Set your legal pages here so that they can be shown at various locations throughout the website."
        )
    ]

    seo_panels = [
        MultiFieldPanel(
            [
                FieldPanel("company_slogan"),
                FieldPanel("company_description"),
            ],
            heading="Company Description",
            help_text="Set some parameters to help with SEO optimisation."
        )
    ]

    socials_and_communications_panel = [
        MultiFieldPanel(
            [
                FieldPanel("business_email"),
            ],
            heading="Business Email",
            help_text="Add your business email address."
        ),
        MultiFieldPanel(
            [
                InlinePanel("social_media_account", label="Social Media Account"),
            ],
            heading="Social Media Accounts",
            help_text="Add your social media accounts."
        )
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(look_and_feel_panels, heading="Look & Feel"),
            ObjectList(legal_compliance_panels, heading="Legal Compliance"),
            ObjectList(socials_and_communications_panel, heading="Socials & Communications"),
            ObjectList(seo_panels, heading="SEO")
        ]
    )

    class Meta:
        """ Meta WebsiteSettings """
        verbose_name = 'Website Settings'
